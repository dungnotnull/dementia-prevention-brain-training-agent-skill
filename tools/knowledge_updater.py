"""
knowledge_updater.py — Skill 236: dementia-prevention-brain-training
======================================================================
Crawl4ai-based knowledge pipeline that fetches the latest peer-reviewed research
and news on dementia prevention, neuroplasticity, and cognitive training, then
appends high-relevance entries to SECOND-KNOWLEDGE-BRAIN.md.

Recommended schedule: Weekly cron job (every Sunday at 08:00 local time)
    0 8 * * 0 python /path/to/236/tools/knowledge_updater.py

Sources crawled:
    - PubMed (NCBI E-utilities API) — peer-reviewed papers
    - Cochrane Library — systematic reviews
    - Alzheimer's Association (alz.org) — research news
    - Lancet Neurology — high-impact research (table of contents)
    - WHO Dementia pages — guideline updates

Requirements:
    pip install crawl4ai requests beautifulsoup4 lxml
    (crawl4ai also requires playwright: playwright install chromium)

Usage:
    python knowledge_updater.py
    python knowledge_updater.py --dry-run   # Preview without writing to brain file
    python knowledge_updater.py --max 20    # Limit entries per run
"""

import os
import re
import sys
import json
import hashlib
import logging
import argparse
import datetime
import time
from typing import Optional
from dataclasses import dataclass, field

# ── Optional dependency guard ────────────────────────────────────────────────
try:
    import requests
    from bs4 import BeautifulSoup
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("WARNING: requests/beautifulsoup4 not installed. Install with: pip install requests beautifulsoup4 lxml")

try:
    import asyncio
    from crawl4ai import AsyncWebCrawler
    CRAWL4AI_AVAILABLE = True
except ImportError:
    CRAWL4AI_AVAILABLE = False
    print("WARNING: crawl4ai not installed. Install with: pip install crawl4ai")

# ── Configuration ─────────────────────────────────────────────────────────────

BRAIN_FILE = os.path.join(
    os.path.dirname(__file__), "..", "SECOND-KNOWLEDGE-BRAIN.md"
)
BRAIN_FILE = os.path.abspath(BRAIN_FILE)

LOG_FILE = os.path.join(os.path.dirname(__file__), "knowledge_updater.log")

# PubMed E-utilities base URL
PUBMED_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
# Optional: set NCBI_API_KEY env var to increase rate limit from 3 to 10 req/sec
NCBI_API_KEY = os.environ.get("NCBI_API_KEY", "")

# Search queries for PubMed
PUBMED_QUERIES = [
    "dementia prevention cognitive training RCT",
    "neuroplasticity elderly intervention brain",
    "FINGER trial cognitive training",
    "dual-task training dementia older adults",
    "N-back working memory aging intervention",
    "BDNF aerobic exercise hippocampus aging",
    "MIND diet Alzheimer prevention",
    "social engagement dementia risk",
    "amyloid sleep glymphatic clearance aging",
    "cognitive reserve Alzheimer prevention",
    "method of loci memory older adults",
    "Alzheimer prevention multidomain intervention",
    "mild cognitive impairment exercise intervention",
]

# Number of PubMed results per query (most recent)
PUBMED_RESULTS_PER_QUERY = 5

# Cochrane search
COCHRANE_QUERIES = [
    "cognitive training dementia prevention",
    "brain training older adults systematic review",
    "exercise dementia prevention systematic review",
    "multidomain intervention cognitive decline",
]

# Domain URLs to crawl for news and updates
DOMAIN_URLS = [
    {
        "url": "https://www.alz.org/research/science/alzheimers-dementia-research",
        "name": "Alzheimer's Association Research News",
        "selector": "article, .news-item, .research-item, h2, h3",
    },
    {
        "url": "https://www.who.int/news-room/fact-sheets/detail/dementia",
        "name": "WHO Dementia Fact Sheet",
        "selector": "article, .sf-detail-body-wrapper, p",
    },
    {
        "url": "https://brainhq.com/brain-resources/brain-training-research/",
        "name": "BrainHQ Research Updates",
        "selector": "article, .research-item, h2, h3, p",
    },
]

# Relevance keywords for scoring (domain-specific)
RELEVANCE_KEYWORDS = [
    "dementia", "alzheimer", "cognitive", "neuroplasticity", "brain training",
    "memory", "cognitive decline", "prevention", "neurodegeneration", "MCI",
    "mild cognitive impairment", "FINGER", "ACTIVE", "BDNF", "hippocampus",
    "N-back", "dual-task", "aerobic exercise", "MIND diet", "cognitive reserve",
    "amyloid", "tau", "sleep", "social engagement", "older adults", "aging",
    "working memory", "episodic memory", "executive function", "attention",
]

# Minimum relevance score to include in brain file (0-10)
MIN_RELEVANCE_SCORE = 5

# Maximum entries to add per run
MAX_ENTRIES_PER_RUN = 30

# Recency scoring cutoffs (years from today)
RECENCY_SCORES = {
    0.5: 10,   # < 6 months old
    1.0: 8,    # < 1 year old
    2.0: 6,    # < 2 years old
    5.0: 4,    # < 5 years old
}
RECENCY_SCORE_OLD = 2  # > 5 years old


# ── Logging ──────────────────────────────────────────────────────────────────

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


# ── Data model ───────────────────────────────────────────────────────────────

@dataclass
class ResearchEntry:
    title: str
    authors: str = ""
    year: int = 0
    venue: str = ""
    doi_or_url: str = ""
    abstract_summary: str = ""
    key_finding: str = ""
    relevance_score: float = 0.0
    domain_tags: list = field(default_factory=list)
    date_added: str = ""
    source_type: str = ""  # pubmed, cochrane, news, guideline

    def to_url_hash(self) -> str:
        """Generate a unique hash for deduplication (based on DOI/URL or title)."""
        key = self.doi_or_url if self.doi_or_url else self.title.lower()
        return hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]

    def to_markdown(self) -> str:
        """Format as SECOND-KNOWLEDGE-BRAIN.md append entry."""
        tags = " ".join(f"#{t.replace(' ', '-')}" for t in self.domain_tags) if self.domain_tags else ""
        return f"""
### {self.title}
- **Authors:** {self.authors or 'N/A'}
- **Year:** {self.year or 'N/A'}
- **Venue:** {self.venue or 'N/A'}
- **DOI/Link:** {self.doi_or_url or 'N/A'}
- **Abstract Summary:** {self.abstract_summary or 'N/A'}
- **Key Finding:** {self.key_finding or 'N/A'}
- **Relevance Score:** {self.relevance_score:.1f}/10
- **Domain Tags:** {tags}
- **Date Added:** {self.date_added}
"""


# ── Deduplication ─────────────────────────────────────────────────────────────

def load_existing_hashes(brain_file: str) -> set:
    """
    Load all existing DOI/URL hashes from the brain file to prevent duplicates.
    Also checks for title substring matches as a fallback.
    """
    existing_hashes = set()
    existing_titles = set()

    if not os.path.exists(brain_file):
        return existing_hashes, existing_titles

    with open(brain_file, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract DOIs and URLs from existing entries
    doi_patterns = re.findall(r"10\.\d{4,}/\S+", content)
    url_patterns = re.findall(r"https?://\S+", content)

    for doi in doi_patterns:
        doi = doi.strip(".,)")
        h = hashlib.sha256(doi.encode("utf-8")).hexdigest()[:16]
        existing_hashes.add(h)

    for url in url_patterns:
        url = url.strip(".,)")
        h = hashlib.sha256(url.encode("utf-8")).hexdigest()[:16]
        existing_hashes.add(h)

    # Extract existing titles (### headings)
    title_patterns = re.findall(r"^### (.+)$", content, re.MULTILINE)
    for t in title_patterns:
        existing_titles.add(t.strip().lower()[:80])

    logger.info(f"Loaded {len(existing_hashes)} existing hashes, {len(existing_titles)} existing titles")
    return existing_hashes, existing_titles


# ── Relevance Scoring ─────────────────────────────────────────────────────────

def calculate_relevance(text: str, year: int = 0) -> float:
    """
    Score entry relevance on a 0-10 scale.
    Formula: keyword_match_score * 6 + recency_score * 4
    Both components are normalized to [0, 1] before weighting.
    """
    text_lower = text.lower()
    matches = sum(1 for kw in RELEVANCE_KEYWORDS if kw.lower() in text_lower)
    keyword_score = min(matches / 5, 1.0)  # Normalize: 5+ matches = max keyword score

    # Recency scoring
    current_year = datetime.datetime.now().year
    age_years = current_year - year if year > 0 else 6  # Unknown year treated as old
    recency_score = RECENCY_SCORE_OLD
    for cutoff, score in sorted(RECENCY_SCORES.items()):
        if age_years <= cutoff:
            recency_score = score
            break
    recency_normalized = recency_score / 10

    final_score = (keyword_score * 6) + (recency_normalized * 4)
    return round(min(final_score, 10.0), 1)


def extract_domain_tags(text: str) -> list:
    """Extract relevant domain tags from text."""
    tag_map = {
        "neuroplasticity": ["neuroplasticity", "brain plasticity", "synaptic"],
        "memory": ["memory", "episodic", "working memory", "recall"],
        "cognitive-training": ["cognitive training", "brain training", "mental exercise"],
        "exercise": ["aerobic", "physical activity", "exercise", "BDNF"],
        "diet": ["MIND diet", "Mediterranean", "nutrition", "omega-3"],
        "sleep": ["sleep", "glymphatic", "amyloid clearance"],
        "social-engagement": ["social", "engagement", "isolation", "social network"],
        "dementia-prevention": ["dementia", "alzheimer", "prevention", "risk reduction"],
        "MCI": ["mild cognitive impairment", "MCI", "subjective cognitive decline"],
        "assessment": ["MMSE", "MoCA", "screening", "assessment", "cognitive test"],
        "dual-task": ["dual-task", "dual task", "concurrent task"],
        "N-back": ["n-back", "n back", "working memory training"],
        "FINGER": ["FINGER", "multidomain intervention", "MAPT"],
    }

    found_tags = []
    text_lower = text.lower()
    for tag, keywords in tag_map.items():
        if any(kw.lower() in text_lower for kw in keywords):
            found_tags.append(tag)

    return found_tags


# ── PubMed Fetcher ────────────────────────────────────────────────────────────

def fetch_pubmed_papers(
    queries: list,
    max_per_query: int = 5,
    min_year: int = 2018,
) -> list[ResearchEntry]:
    """
    Fetch recent papers from PubMed using NCBI E-utilities API.
    No authentication required for basic access (10 req/sec with API key).
    """
    if not REQUESTS_AVAILABLE:
        logger.warning("requests not available — skipping PubMed fetch")
        return []

    entries = []
    today = datetime.datetime.now()

    for query in queries:
        try:
            logger.info(f"PubMed search: {query}")

            # Step 1: ESearch — get PMIDs
            search_url = f"{PUBMED_BASE}/esearch.fcgi"
            search_params = {
                "db": "pubmed",
                "term": f"{query} AND ({min_year}[PDAT]:3000[PDAT])",
                "retmax": max_per_query,
                "sort": "pub+date",
                "retmode": "json",
            }
            if NCBI_API_KEY:
                search_params["api_key"] = NCBI_API_KEY

            r = requests.get(search_url, params=search_params, timeout=15)
            r.raise_for_status()
            search_data = r.json()

            pmids = search_data.get("esearchresult", {}).get("idlist", [])
            if not pmids:
                logger.info(f"  No results for query: {query}")
                continue

            # Step 2: EFetch — get details for each PMID
            fetch_url = f"{PUBMED_BASE}/efetch.fcgi"
            fetch_params = {
                "db": "pubmed",
                "id": ",".join(pmids),
                "rettype": "xml",
                "retmode": "xml",
            }
            if NCBI_API_KEY:
                fetch_params["api_key"] = NCBI_API_KEY

            time.sleep(0.5)  # Rate limiting (3 req/sec without API key)
            r2 = requests.get(fetch_url, params=fetch_params, timeout=30)
            r2.raise_for_status()

            soup = BeautifulSoup(r2.content, "lxml-xml")
            articles = soup.find_all("PubmedArticle")

            for article in articles:
                try:
                    # Title
                    title_tag = article.find("ArticleTitle")
                    title = title_tag.get_text(strip=True) if title_tag else "Untitled"

                    # Authors
                    authors_list = []
                    for author in article.find_all("Author")[:4]:
                        last = author.find("LastName")
                        first = author.find("ForeName")
                        if last:
                            name = last.get_text()
                            if first:
                                name += f" {first.get_text()[0]}"
                            authors_list.append(name)
                    if len(article.find_all("Author")) > 4:
                        authors_list.append("et al.")
                    authors = "; ".join(authors_list)

                    # Year
                    year_tag = article.find("PubDate")
                    year = 0
                    if year_tag:
                        y = year_tag.find("Year")
                        if y:
                            year = int(y.get_text())

                    # Journal
                    journal_tag = article.find("Title")  # Journal Title
                    journal = journal_tag.get_text(strip=True) if journal_tag else ""

                    # PMID → DOI link
                    pmid_tag = article.find("PMID")
                    pmid = pmid_tag.get_text() if pmid_tag else ""
                    doi_tag = article.find("ELocationID", {"EIdType": "doi"})
                    if doi_tag:
                        doi = f"https://doi.org/{doi_tag.get_text()}"
                    else:
                        doi = f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/" if pmid else ""

                    # Abstract
                    abstract_tag = article.find("AbstractText")
                    abstract = abstract_tag.get_text(strip=True) if abstract_tag else ""
                    abstract_summary = abstract[:300] + "..." if len(abstract) > 300 else abstract

                    # Key finding — first sentence of abstract or conclusion section
                    conclusion_tag = article.find("AbstractText", {"Label": "CONCLUSIONS"})
                    if conclusion_tag:
                        key_finding = conclusion_tag.get_text(strip=True)[:200]
                    elif abstract:
                        sentences = abstract.split(". ")
                        key_finding = sentences[-1][:200] if sentences else abstract[:200]
                    else:
                        key_finding = ""

                    # Relevance score
                    full_text = f"{title} {abstract} {journal}"
                    relevance = calculate_relevance(full_text, year)

                    if relevance < MIN_RELEVANCE_SCORE:
                        logger.debug(f"  Skipped (low relevance {relevance}): {title[:60]}")
                        continue

                    domain_tags = extract_domain_tags(full_text)
                    date_added = today.strftime("%Y-%m-%d")

                    entry = ResearchEntry(
                        title=title,
                        authors=authors,
                        year=year,
                        venue=journal,
                        doi_or_url=doi,
                        abstract_summary=abstract_summary,
                        key_finding=key_finding,
                        relevance_score=relevance,
                        domain_tags=domain_tags,
                        date_added=date_added,
                        source_type="pubmed",
                    )
                    entries.append(entry)
                    logger.info(f"  Found: [{relevance}] {title[:70]}...")

                except Exception as e:
                    logger.warning(f"  Error parsing article: {e}")
                    continue

            time.sleep(1.0)  # PubMed rate limit

        except Exception as e:
            logger.error(f"PubMed query failed ({query}): {e}")
            continue

    return entries


# ── Cochrane Fetcher ──────────────────────────────────────────────────────────

async def fetch_cochrane_reviews(queries: list) -> list[ResearchEntry]:
    """
    Fetch systematic review listings from Cochrane Library using crawl4ai.
    Cochrane does not have a public API, so we crawl the search page.
    """
    if not CRAWL4AI_AVAILABLE:
        logger.warning("crawl4ai not available — skipping Cochrane fetch")
        return []

    entries = []
    today = datetime.datetime.now()

    async with AsyncWebCrawler(verbose=False) as crawler:
        for query in queries:
            try:
                search_url = (
                    f"https://www.cochranelibrary.com/search?"
                    f"p_p_id=scolarissearchresultsportlet_WAR_scolarissearchresults&"
                    f"q={query.replace(' ', '+')}&t=13"  # t=13 = Systematic Reviews
                )
                logger.info(f"Cochrane search: {query}")

                result = await crawler.arun(url=search_url, timeout=30)
                if not result.success:
                    logger.warning(f"Cochrane crawl failed for: {query}")
                    continue

                soup = BeautifulSoup(result.html, "lxml")

                # Parse search result items
                items = soup.select(".search-results-item, .result-item, article")
                if not items:
                    # Fallback: look for heading + text blocks
                    items = soup.select("h3, h4")

                for item in items[:3]:  # Limit per query
                    title_el = item.find(["h3", "h4", "a"])
                    title = title_el.get_text(strip=True) if title_el else item.get_text(strip=True)[:100]

                    if len(title) < 10:
                        continue

                    url_el = item.find("a", href=True)
                    url = ""
                    if url_el:
                        href = url_el["href"]
                        url = href if href.startswith("http") else f"https://www.cochranelibrary.com{href}"

                    # Extract year from text if visible
                    text = item.get_text()
                    year_match = re.search(r"\b(201[5-9]|202[0-9])\b", text)
                    year = int(year_match.group()) if year_match else 0

                    full_text = f"{title} {text} dementia prevention systematic review"
                    relevance = calculate_relevance(full_text, year)

                    if relevance < MIN_RELEVANCE_SCORE:
                        continue

                    entry = ResearchEntry(
                        title=title,
                        authors="Cochrane Review",
                        year=year,
                        venue="Cochrane Database of Systematic Reviews",
                        doi_or_url=url,
                        abstract_summary=f"Cochrane systematic review on: {query}",
                        key_finding="See full review for findings.",
                        relevance_score=relevance,
                        domain_tags=extract_domain_tags(full_text),
                        date_added=today.strftime("%Y-%m-%d"),
                        source_type="cochrane",
                    )
                    entries.append(entry)
                    logger.info(f"  Found Cochrane: [{relevance}] {title[:70]}")

            except Exception as e:
                logger.error(f"Cochrane fetch error ({query}): {e}")

    return entries


# ── Domain URL Fetcher ────────────────────────────────────────────────────────

async def fetch_domain_urls(domain_configs: list) -> list[ResearchEntry]:
    """
    Crawl specific domain URLs for research news and guideline updates using crawl4ai.
    """
    if not CRAWL4AI_AVAILABLE:
        logger.warning("crawl4ai not available — skipping domain URL fetch")
        return []

    entries = []
    today = datetime.datetime.now()

    async with AsyncWebCrawler(verbose=False) as crawler:
        for config in domain_configs:
            url = config["url"]
            name = config["name"]
            selector = config.get("selector", "article, p, h2, h3")

            try:
                logger.info(f"Crawling: {name} ({url})")
                result = await crawler.arun(url=url, timeout=30)

                if not result.success:
                    logger.warning(f"Crawl failed: {url}")
                    continue

                soup = BeautifulSoup(result.html, "lxml")

                # Use markdown content if available (crawl4ai provides this)
                text_content = result.markdown if hasattr(result, "markdown") and result.markdown else result.html

                # Extract headings that look like article/paper titles
                elements = soup.select(selector)
                seen_titles = set()

                for el in elements[:20]:
                    title = el.get_text(strip=True)
                    if len(title) < 15 or len(title) > 200:
                        continue
                    if title.lower() in seen_titles:
                        continue

                    seen_titles.add(title.lower())

                    # Check relevance
                    relevance = calculate_relevance(f"{title} {text_content[:500]}", today.year)
                    if relevance < MIN_RELEVANCE_SCORE:
                        continue

                    # Try to find a link
                    link_el = el.find("a", href=True)
                    link = ""
                    if link_el:
                        href = link_el["href"]
                        link = href if href.startswith("http") else f"{url.rstrip('/')}/{href.lstrip('/')}"

                    entry = ResearchEntry(
                        title=title,
                        authors="",
                        year=today.year,
                        venue=name,
                        doi_or_url=link or url,
                        abstract_summary=f"From {name}: {title[:200]}",
                        key_finding="See source URL for full details.",
                        relevance_score=relevance,
                        domain_tags=extract_domain_tags(title),
                        date_added=today.strftime("%Y-%m-%d"),
                        source_type="news",
                    )
                    entries.append(entry)

            except Exception as e:
                logger.error(f"Domain URL fetch error ({url}): {e}")

    return entries


# ── Brain File Writer ─────────────────────────────────────────────────────────

def append_to_brain_file(
    entries: list[ResearchEntry],
    brain_file: str,
    existing_hashes: set,
    existing_titles: set,
    dry_run: bool = False,
) -> int:
    """
    Append new, non-duplicate entries to SECOND-KNOWLEDGE-BRAIN.md.
    Returns the count of entries actually appended.
    """
    if not entries:
        logger.info("No entries to append.")
        return 0

    today = datetime.datetime.now().strftime("%Y-%m-%d")
    new_entries = []
    skipped_count = 0

    for entry in entries:
        url_hash = entry.to_url_hash()
        title_key = entry.title.strip().lower()[:80]

        if url_hash in existing_hashes:
            logger.debug(f"Duplicate (hash): {entry.title[:60]}")
            skipped_count += 1
            continue

        if title_key in existing_titles:
            logger.debug(f"Duplicate (title): {entry.title[:60]}")
            skipped_count += 1
            continue

        new_entries.append(entry)
        existing_hashes.add(url_hash)
        existing_titles.add(title_key)

    logger.info(f"New entries: {len(new_entries)} | Duplicates skipped: {skipped_count}")

    if not new_entries:
        return 0

    if dry_run:
        logger.info("[DRY RUN] Would append the following entries:")
        for e in new_entries:
            logger.info(f"  - [{e.relevance_score}] {e.title[:70]}")
        return len(new_entries)

    # Sort by relevance score descending
    new_entries.sort(key=lambda e: e.relevance_score, reverse=True)

    # Build markdown block to append
    update_section = f"\n\n---\n\n## Knowledge Update — {today}\n\n"
    update_section += f"*{len(new_entries)} new entries added from automated crawl*\n"
    update_section += f"*Sources: PubMed, Cochrane Library, Alzheimer's Association, WHO*\n"

    for entry in new_entries:
        update_section += entry.to_markdown()

    # Append to brain file
    with open(brain_file, "a", encoding="utf-8") as f:
        f.write(update_section)

    # Update the Knowledge Update Log table
    update_log_entry = (
        f"\n| {today} | PubMed + Cochrane + Domain URLs | "
        f"{len(new_entries)} | "
        f"Automated weekly crawl — dementia prevention, neuroplasticity, cognitive training |"
    )

    # Insert into the Knowledge Update Log section
    with open(brain_file, "r", encoding="utf-8") as f:
        content = f.read()

    if "## 8. Knowledge Update Log" in content:
        # Append row to the log table (after last | row)
        log_section_start = content.index("## 8. Knowledge Update Log")
        insert_pos = content.rfind("|", log_section_start)
        if insert_pos > 0:
            # Find end of that row
            row_end = content.index("\n", insert_pos)
            new_content = content[:row_end + 1] + update_log_entry + content[row_end + 1:]
            with open(brain_file, "w", encoding="utf-8") as f:
                f.write(new_content)

    logger.info(f"Successfully appended {len(new_entries)} entries to {brain_file}")
    return len(new_entries)


# ── Main Orchestrator ─────────────────────────────────────────────────────────

async def run_update(dry_run: bool = False, max_entries: int = MAX_ENTRIES_PER_RUN):
    """Main update pipeline — fetch from all sources and append to brain file."""
    start_time = datetime.datetime.now()
    logger.info("=" * 60)
    logger.info(f"knowledge_updater.py — START — {start_time.isoformat()}")
    logger.info(f"Brain file: {BRAIN_FILE}")
    logger.info(f"Dry run: {dry_run}")
    logger.info("=" * 60)

    # Load existing entries for deduplication
    existing_hashes, existing_titles = load_existing_hashes(BRAIN_FILE)

    all_entries: list[ResearchEntry] = []

    # 1. PubMed
    logger.info("\n--- Fetching from PubMed ---")
    pubmed_entries = fetch_pubmed_papers(
        PUBMED_QUERIES,
        max_per_query=PUBMED_RESULTS_PER_QUERY,
        min_year=2018,
    )
    logger.info(f"PubMed: {len(pubmed_entries)} candidate entries")
    all_entries.extend(pubmed_entries)

    # 2. Cochrane
    logger.info("\n--- Fetching from Cochrane Library ---")
    cochrane_entries = await fetch_cochrane_reviews(COCHRANE_QUERIES)
    logger.info(f"Cochrane: {len(cochrane_entries)} candidate entries")
    all_entries.extend(cochrane_entries)

    # 3. Domain URLs (news and guidelines)
    logger.info("\n--- Fetching from Domain URLs ---")
    domain_entries = await fetch_domain_urls(DOMAIN_URLS)
    logger.info(f"Domain URLs: {len(domain_entries)} candidate entries")
    all_entries.extend(domain_entries)

    # Sort all candidates by relevance (best first) and cap at max_entries
    all_entries.sort(key=lambda e: e.relevance_score, reverse=True)
    all_entries = all_entries[:max_entries]

    logger.info(f"\nTotal candidate entries (after cap): {len(all_entries)}")

    # Append to brain file
    logger.info("\n--- Appending to SECOND-KNOWLEDGE-BRAIN.md ---")
    appended = append_to_brain_file(
        all_entries,
        BRAIN_FILE,
        existing_hashes,
        existing_titles,
        dry_run=dry_run,
    )

    elapsed = (datetime.datetime.now() - start_time).total_seconds()
    logger.info(f"\n{'=' * 60}")
    logger.info(f"DONE — {appended} entries appended in {elapsed:.1f}s")
    logger.info(f"{'=' * 60}\n")

    return appended


# ── Entry Point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Crawl4ai knowledge updater for dementia-prevention-brain-training skill"
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Preview entries without writing to brain file",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=MAX_ENTRIES_PER_RUN,
        help=f"Maximum entries to add per run (default: {MAX_ENTRIES_PER_RUN})",
    )
    args = parser.parse_args()

    if not REQUESTS_AVAILABLE:
        logger.error("requests and beautifulsoup4 are required. Install: pip install requests beautifulsoup4 lxml")

    if not CRAWL4AI_AVAILABLE:
        logger.warning("crawl4ai not available — Cochrane and domain URL crawls will be skipped")
        if not REQUESTS_AVAILABLE:
            logger.error("Neither requests nor crawl4ai is available. Cannot proceed.")
            sys.exit(1)

    # Run async main
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(run_update(dry_run=args.dry_run, max_entries=args.max))


if __name__ == "__main__":
    main()


# ── Cron Setup (Reference) ───────────────────────────────────────────────────
# Add to crontab (Unix/Linux/Mac): crontab -e
# Run every Sunday at 08:00:
#   0 8 * * 0 cd /path/to/236/tools && /usr/bin/python3 knowledge_updater.py >> knowledge_updater.log 2>&1
#
# Windows Task Scheduler (PowerShell):
#   $action = New-ScheduledTaskAction -Execute "python" -Argument "D:\Dungchan\skill_adv\236\tools\knowledge_updater.py"
#   $trigger = New-ScheduledTaskTrigger -Weekly -DaysOfWeek Sunday -At 8am
#   Register-ScheduledTask -Action $action -Trigger $trigger -TaskName "BrainTrainingKnowledgeUpdater"
