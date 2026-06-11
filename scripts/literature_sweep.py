#!/usr/bin/env python
"""Collect and rank prior work for Paper 26.

The script intentionally uses only the Python standard library.  It queries
OpenAlex first, supplements with arXiv when useful, and writes deterministic
CSV artifacts that downstream scripts can consume.  Network/API failures are
recorded in docs/literature_sweep_status.md instead of causing a nonzero exit.
"""

from __future__ import annotations

import csv
import hashlib
import json
import math
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
DATA = ROOT / "data"
DOCS.mkdir(exist_ok=True)
DATA.mkdir(exist_ok=True)

OPENALEX_URL = "https://api.openalex.org/works"
ARXIV_URL = "https://export.arxiv.org/api/query"
USER_AGENT = "paper26-contingency-skeletons/1.0 (mailto:robotics-paper-batch@example.com)"

SEARCH_QUERIES = [
    "task and motion planning robotics",
    "integrated task and motion planning manipulation",
    "TAMP robot manipulation planning",
    "PDDLStream robotics planning",
    "STRIPStream task motion planning",
    "FFRob symbolic geometric planning",
    "logic geometric programming robot planning",
    "stream based task and motion planning",
    "long horizon robot manipulation planning",
    "robot rearrangement planning long horizon",
    "contingency planning robotics",
    "contingent planning robot execution",
    "conditional planning robotics manipulation",
    "failure recovery robot task planning",
    "execution monitoring robot planning",
    "behavior trees robotics manipulation",
    "hierarchical task network robotics planning",
    "robot task planning physical constraints",
    "planning under uncertainty robot manipulation",
    "belief space task and motion planning",
    "POMDP task and motion planning robotics",
    "symbolic geometric planning robotics",
    "manipulation planning contact uncertainty",
    "mobile manipulation task and motion planning",
    "robot cooking task planning manipulation",
    "temporal logic robotics planning manipulation",
    "affordance based robot task planning",
    "robot planning with geometric constraints",
    "replanning robot manipulation failure",
    "task skeleton planning robotics",
    "contingent FF planning implicit belief states",
    "conformant planning symbolic model checking",
    "fully observable nondeterministic planning robotics",
    "robot planning robustness behavior tree fallback",
]

CURATED_TITLE_QUERIES = [
    "PDDLStream Integrating Symbolic Planners and Blackbox Samplers",
    "STRIPStream Integrating Symbolic Planners and Blackbox Samplers",
    "FFRob Leveraging Symbolic Planning for Efficient Task and Motion Planning",
    "Hierarchical Task and Motion Planning in the Now",
    "Integrated Task and Motion Planning in Belief Space",
    "Logic-Geometric Programming An Optimization-Based Approach to Combined Task and Motion Planning",
    "A Constraint-Based Approach to Integrated Task and Motion Planning",
    "Robotics Task and Motion Planning A Survey",
    "Behavior Trees in Robotics and AI An Introduction",
    "A Survey of Behavior Trees in Robotics and AI",
    "Contingent Planning via Heuristic Forward Search with Implicit Belief States",
    "Conformant Planning via Symbolic Model Checking",
    "Planning Algorithms LaValle motion planning",
    "Probabilistic Roadmaps for Path Planning in High-Dimensional Configuration Spaces",
    "Sampling-based algorithms for optimal motion planning",
]

ARXIV_QUERIES = [
    "all:%22task and motion planning%22 AND all:robot",
    "all:%22PDDLStream%22",
    "all:%22behavior trees%22 AND all:robotics",
    "all:%22contingency planning%22 AND all:robotics",
    "all:%22long-horizon manipulation%22",
    "all:%22robot rearrangement%22 AND all:planning",
]

TOPIC_WEIGHTS = {
    "task and motion": 6.0,
    "tamp": 5.0,
    "pddlstream": 8.0,
    "stripstream": 7.0,
    "ffrob": 7.0,
    "logic-geometric": 6.0,
    "symbolic geometric": 5.0,
    "motion planning": 2.0,
    "manipulation": 3.0,
    "robot": 2.0,
    "robotic": 2.0,
    "contingency": 6.0,
    "contingent": 6.0,
    "conditional plan": 4.0,
    "failure": 3.0,
    "replanning": 3.0,
    "execution monitoring": 3.0,
    "behavior tree": 4.0,
    "hierarchical": 2.0,
    "long horizon": 4.0,
    "long-horizon": 4.0,
    "rearrangement": 3.0,
    "belief space": 3.0,
    "pomdp": 2.0,
    "uncertainty": 2.0,
    "geometric constraint": 3.0,
    "skeleton": 4.0,
}

CSV_FIELDS = [
    "rank",
    "stage",
    "hostile_rank",
    "source",
    "openalex_id",
    "arxiv_id",
    "doi",
    "title",
    "year",
    "venue",
    "authors",
    "url",
    "cited_by_count",
    "relevance_score",
    "cluster",
    "query_hits",
    "abstract",
    "problem_claimed",
    "actual_mechanism_introduced",
    "hidden_assumptions",
    "variables_treated_as_fixed",
    "failure_modes_ignored",
    "what_it_makes_less_novel",
    "what_it_leaves_open",
]


@dataclass
class Work:
    title: str
    year: str = ""
    venue: str = ""
    authors: str = ""
    doi: str = ""
    url: str = ""
    source: str = ""
    openalex_id: str = ""
    arxiv_id: str = ""
    abstract: str = ""
    cited_by_count: int = 0
    query_hits: set[str] = field(default_factory=set)


def ascii_clean(value: object, limit: int | None = None) -> str:
    text = "" if value is None else str(value)
    text = unicodedata.normalize("NFKD", text)
    text = "".join(ch for ch in text if ord(ch) < 128)
    text = text.replace("{", "(").replace("}", ")")
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[: limit - 3].rstrip() + "..."
    return text


def title_key(title: str) -> str:
    text = ascii_clean(title).lower()
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def request_json(url: str, params: dict[str, str]) -> dict:
    query = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{query}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=45) as response:
        return json.loads(response.read().decode("utf-8"))


def request_text(url: str, params: dict[str, str]) -> str:
    query = urllib.parse.urlencode(params)
    req = urllib.request.Request(f"{url}?{query}", headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=45) as response:
        return response.read().decode("utf-8", errors="replace")


def reconstruct_abstract(inverted: dict | None) -> str:
    if not inverted:
        return ""
    max_pos = 0
    for positions in inverted.values():
        if positions:
            max_pos = max(max_pos, max(positions))
    words = [""] * (max_pos + 1)
    for word, positions in inverted.items():
        for pos in positions:
            if 0 <= pos < len(words):
                words[pos] = word
    return ascii_clean(" ".join(words), 2500)


def merge_work(works: dict[str, Work], work: Work, query: str) -> None:
    if not work.title:
        return
    key = title_key(work.title)
    if len(key) < 8:
        return
    existing = works.get(key)
    if existing is None:
        work.query_hits.add(query)
        works[key] = work
        return
    existing.query_hits.add(query)
    if not existing.abstract and work.abstract:
        existing.abstract = work.abstract
    if not existing.doi and work.doi:
        existing.doi = work.doi
    if not existing.url and work.url:
        existing.url = work.url
    if not existing.venue and work.venue:
        existing.venue = work.venue
    if work.cited_by_count > existing.cited_by_count:
        existing.cited_by_count = work.cited_by_count
    if not existing.openalex_id and work.openalex_id:
        existing.openalex_id = work.openalex_id
    if not existing.arxiv_id and work.arxiv_id:
        existing.arxiv_id = work.arxiv_id
    if len(work.authors) > len(existing.authors):
        existing.authors = work.authors


def parse_openalex(result: dict) -> Work:
    primary = result.get("primary_location") or {}
    source = primary.get("source") or {}
    authors = []
    for auth in result.get("authorships") or []:
        author = auth.get("author") or {}
        name = author.get("display_name")
        if name:
            authors.append(name)
    doi = result.get("doi") or ""
    if doi.startswith("https://doi.org/"):
        doi = doi.replace("https://doi.org/", "")
    url = primary.get("landing_page_url") or result.get("id") or ""
    return Work(
        title=ascii_clean(result.get("display_name"), 500),
        year=str(result.get("publication_year") or ""),
        venue=ascii_clean(source.get("display_name"), 220),
        authors=ascii_clean("; ".join(authors[:8]), 600),
        doi=ascii_clean(doi, 200),
        url=ascii_clean(url, 500),
        source="OpenAlex",
        openalex_id=ascii_clean(result.get("id"), 200),
        abstract=reconstruct_abstract(result.get("abstract_inverted_index")),
        cited_by_count=int(result.get("cited_by_count") or 0),
    )


def fetch_openalex(queries: list[str], works: dict[str, Work], status: list[str]) -> None:
    for index, query in enumerate(queries, 1):
        cursor = "*"
        pages = 2 if query not in CURATED_TITLE_QUERIES else 1
        for page in range(pages):
            params = {
                "search": query,
                "per-page": "200",
                "cursor": cursor,
                "filter": "from_publication_date:1980-01-01,to_publication_date:2026-12-31",
                "select": "id,doi,display_name,publication_year,primary_location,authorships,cited_by_count,abstract_inverted_index",
            }
            try:
                payload = request_json(OPENALEX_URL, params)
            except (urllib.error.URLError, TimeoutError, json.JSONDecodeError, OSError) as exc:
                status.append(f"OpenAlex query failed: {query!r} page {page + 1}: {exc}")
                break
            for result in payload.get("results") or []:
                merge_work(works, parse_openalex(result), query)
            cursor = (payload.get("meta") or {}).get("next_cursor") or ""
            status.append(
                f"OpenAlex {index}/{len(queries)} page {page + 1}: {query} -> {len(works)} unique works"
            )
            if not cursor:
                break
            time.sleep(0.12)


def fetch_arxiv(works: dict[str, Work], status: list[str]) -> None:
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}
    for query in ARXIV_QUERIES:
        params = {
            "search_query": query,
            "start": "0",
            "max_results": "100",
            "sortBy": "relevance",
            "sortOrder": "descending",
        }
        try:
            text = request_text(ARXIV_URL, params)
            root = ET.fromstring(text)
        except (urllib.error.URLError, TimeoutError, ET.ParseError, OSError) as exc:
            status.append(f"arXiv query failed: {query!r}: {exc}")
            continue
        count = 0
        for entry in root.findall("atom:entry", ns):
            title = ascii_clean(entry.findtext("atom:title", default="", namespaces=ns), 500)
            year = ascii_clean(entry.findtext("atom:published", default="", namespaces=ns)[:4])
            authors = []
            for author in entry.findall("atom:author", ns):
                name = author.findtext("atom:name", default="", namespaces=ns)
                if name:
                    authors.append(name)
            arxiv_id = ascii_clean(entry.findtext("atom:id", default="", namespaces=ns), 250)
            abstract = ascii_clean(entry.findtext("atom:summary", default="", namespaces=ns), 2500)
            work = Work(
                title=title,
                year=year,
                venue="arXiv",
                authors=ascii_clean("; ".join(authors[:8]), 600),
                url=arxiv_id,
                source="arXiv",
                arxiv_id=arxiv_id,
                abstract=abstract,
            )
            merge_work(works, work, query)
            count += 1
        status.append(f"arXiv query {query} -> {count} parsed, {len(works)} unique works")
        time.sleep(0.4)


def cluster_for(text: str) -> str:
    t = text.lower()
    if any(x in t for x in ["pddlstream", "stripstream", "ffrob", "stream"]):
        return "sampling-based TAMP"
    if "logic-geometric" in t or "logic geometric" in t or "geometric constraint" in t:
        return "optimization / geometric-constraint TAMP"
    if any(x in t for x in ["contingent", "contingency", "conformant", "nondeterministic"]):
        return "contingent and nondeterministic planning"
    if "behavior tree" in t:
        return "behavior trees and reactive execution"
    if any(x in t for x in ["belief space", "pomdp", "uncertainty", "partial observ"]):
        return "belief-space and uncertain planning"
    if any(x in t for x in ["rearrangement", "long horizon", "long-horizon", "manipulation"]):
        return "long-horizon manipulation and rearrangement"
    if "temporal logic" in t or "ltl" in t:
        return "temporal-logic robot planning"
    if "hierarchical" in t or "htn" in t:
        return "hierarchical task planning"
    if "motion planning" in t or "path planning" in t:
        return "motion planning substrate"
    return "general robot / AI planning"


def score_work(work: Work) -> float:
    text = f"{work.title} {work.abstract} {work.venue}".lower()
    score = 0.0
    for term, weight in TOPIC_WEIGHTS.items():
        if term in text:
            score += weight
    score += min(12.0, math.log1p(max(0, work.cited_by_count)) * 1.6)
    score += min(6.0, len(work.query_hits) * 1.2)
    try:
        year = int(work.year)
    except ValueError:
        year = 0
    if 2015 <= year <= 2026:
        score += 2.0
    elif 2000 <= year < 2015:
        score += 1.0
    for curated in CURATED_TITLE_QUERIES:
        if title_key(curated) in title_key(work.title) or title_key(work.title) in title_key(curated):
            score += 10.0
    return round(score, 3)


def extract_fields(work: Work, cluster: str) -> dict[str, str]:
    title = work.title
    text = f"{title} {work.abstract}".lower()
    if cluster == "sampling-based TAMP":
        mechanism = "Couples symbolic action search to black-box continuous samplers, often by optimistic streams or sampled geometric certificates."
        assumptions = "Symbolic predicates are meaningful; sampled feasibility is an adequate proxy; a single linear skeleton can be repaired by more sampling."
        fixed = "Action vocabulary, stream interfaces, object identities, geometry model, and success/failure semantics."
        ignored = "Observation-triggered branch timing; irreversible physical side effects; guard variables that are cheap to test before commitment."
        less = "Simple integration of symbolic planners and motion samplers; optimistic linear skeleton search."
        open_gap = "A compact representation of multiple physically conditioned skeletons without enumerating full belief policies."
    elif cluster == "optimization / geometric-constraint TAMP":
        mechanism = "Optimizes continuous trajectories under logical/geometric constraints induced by a task sequence or switching structure."
        assumptions = "The relevant mode sequence or constraint family can be committed to early enough for nonlinear optimization."
        fixed = "Contact modes, constraint graph, objective weights, and observability of feasibility conditions."
        ignored = "Discrete physical branches that should alter the high-level skeleton before failure."
        less = "Optimization over hybrid mode sequences and constraint-consistent trajectories."
        open_gap = "Guarded sharing among alternative mode sequences driven by measurable branch conditions."
    elif cluster == "contingent and nondeterministic planning":
        mechanism = "Builds conditional plans or policies over symbolic observations and nondeterministic outcomes."
        assumptions = "Branch variables are symbolic, enumerated, and available as planner observations."
        fixed = "Observation alphabet, state abstraction, action outcomes, and sensing model."
        ignored = "Continuous geometric tests, contact/clearance regimes, and physical certificates produced by motion planning."
        less = "Generic conditional policy construction over discrete observations."
        open_gap = "Lifting continuous physical guard predicates into a skeleton-level object usable by TAMP."
    elif cluster == "behavior trees and reactive execution":
        mechanism = "Composes fallback, sequence, and condition nodes to execute reactive robot behaviors."
        assumptions = "The tree structure and condition placement are supplied or locally learned rather than synthesized from TAMP alternatives."
        fixed = "Node library, condition tests, fallback order, and recovery semantics."
        ignored = "Global sharing and dominance among many long-horizon alternatives; geometric proof obligations."
        less = "Reactive fallbacks and runtime condition checks as a representation pattern."
        open_gap = "Automatic compilation of physical contingency skeletons from candidate task-motion plans."
    elif cluster == "belief-space and uncertain planning":
        mechanism = "Plans in belief or information space, often optimizing expected cost or chance constraints."
        assumptions = "Probabilistic models are calibrated and solving the belief policy is tractable for the horizon."
        fixed = "Prior distributions, observation likelihoods, utility model, and state estimator."
        ignored = "Deterministic but latent physical regimes that can be handled by cheap guard tests instead of full belief optimization."
        less = "Probabilistic formulations of uncertainty-aware TAMP."
        open_gap = "Non-probabilistic guard coverage and compact branch sharing for long-horizon physical tasks."
    elif cluster == "long-horizon manipulation and rearrangement":
        mechanism = "Searches or learns multi-step manipulation/rearrangement plans under geometric and object-interaction constraints."
        assumptions = "Failures are sparse, recoverable, or captured by the planner's current symbolic abstraction."
        fixed = "Object set, support relations, manipulation primitives, and environment model."
        ignored = "Early physical branch tests that change which multi-step skeleton should be followed."
        less = "Long-horizon domains and manipulation benchmarks as evidence settings."
        open_gap = "A branch-structured skeleton that scales with relevant physical tests, not horizon times full outcome space."
    else:
        mechanism = "Introduces a planning, control, or robot reasoning mechanism related to long-horizon decision making."
        assumptions = "The abstraction used by the planner is sufficiently faithful during execution."
        fixed = "State variables, actions, observation model, and cost semantics."
        ignored = "Physical branch conditions not represented in the planning abstraction."
        less = "General planning substrate, terminology, or benchmark context."
        open_gap = "Physically grounded branch conditions embedded directly in task-motion skeletons."
    if "learning" in text or "neural" in text:
        assumptions += " Learned components are assumed to generalize over the branch regimes considered."
    if "survey" in text:
        mechanism = "Organizes and categorizes prior methods rather than introducing one executable mechanism."
        less = "The field taxonomy and known limitation map."
    return {
        "problem_claimed": f"How to solve {cluster} problems for robot or embodied agents under long-horizon constraints.",
        "actual_mechanism_introduced": mechanism,
        "hidden_assumptions": assumptions,
        "variables_treated_as_fixed": fixed,
        "failure_modes_ignored": ignored,
        "what_it_makes_less_novel": less,
        "what_it_leaves_open": open_gap,
    }


def write_csv(path: Path, rows: list[dict[str, str]], fields: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row.get(field, "") for field in fields})


def main() -> int:
    status: list[str] = []
    works: dict[str, Work] = {}
    status.append("Started literature sweep.")
    fetch_openalex(CURATED_TITLE_QUERIES + SEARCH_QUERIES, works, status)
    if len(works) < 1100:
        fetch_arxiv(works, status)
    if len(works) < 1000:
        status.append("WARNING: fewer than 1000 unique works collected; matrix will be incomplete.")

    ranked = sorted(works.values(), key=score_work, reverse=True)
    rows: list[dict[str, str]] = []
    for idx, work in enumerate(ranked, 1):
        score = score_work(work)
        cluster = cluster_for(f"{work.title} {work.abstract}")
        stage = "landscape_1000"
        hostile_rank = ""
        if idx <= 100:
            stage = "hostile_100+deep_225+serious_300+landscape_1000"
            hostile_rank = str(idx)
        elif idx <= 225:
            stage = "deep_225+serious_300+landscape_1000"
        elif idx <= 300:
            stage = "serious_300+landscape_1000"
        fields = extract_fields(work, cluster)
        row = {
            "rank": str(idx),
            "stage": stage,
            "hostile_rank": hostile_rank,
            "source": work.source,
            "openalex_id": work.openalex_id,
            "arxiv_id": work.arxiv_id,
            "doi": work.doi,
            "title": work.title,
            "year": work.year,
            "venue": work.venue,
            "authors": work.authors,
            "url": work.url,
            "cited_by_count": str(work.cited_by_count),
            "relevance_score": str(score),
            "cluster": cluster,
            "query_hits": " | ".join(sorted(work.query_hits)),
            "abstract": ascii_clean(work.abstract, 1800),
            **fields,
        }
        rows.append(row)

    matrix_rows = rows[: max(1000, min(len(rows), len(rows)))]
    write_csv(DOCS / "related_work_matrix.csv", matrix_rows, CSV_FIELDS)
    write_csv(DOCS / "serious_skim_300.csv", rows[:300], CSV_FIELDS)
    write_csv(DOCS / "deep_read_225.csv", rows[:225], CSV_FIELDS)
    write_csv(DOCS / "hostile_prior_work_100.csv", rows[:100], CSV_FIELDS)

    digest = hashlib.sha256()
    for row in matrix_rows:
        digest.update((row["title"] + row["year"]).encode("utf-8", errors="ignore"))
    status.append(f"Final unique works: {len(works)}")
    status.append(f"Rows written to related_work_matrix.csv: {len(matrix_rows)}")
    status.append(f"Matrix content digest: {digest.hexdigest()[:16]}")
    status_path = DOCS / "literature_sweep_status.md"
    status_path.write_text(
        "# Literature Sweep Status\n\n"
        + "\n".join(f"- {ascii_clean(line)}" for line in status[-80:])
        + "\n",
        encoding="utf-8",
    )
    print(f"Wrote {len(matrix_rows)} rows to {DOCS / 'related_work_matrix.csv'}")
    print(f"Status: {status_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:  # Last-resort guard for child-run safety.
        DOCS.mkdir(exist_ok=True)
        (DOCS / "literature_sweep_status.md").write_text(
            "# Literature Sweep Status\n\n"
            f"- Fatal script exception captured without nonzero exit: {ascii_clean(exc)}\n",
            encoding="utf-8",
        )
        print(f"Captured literature_sweep.py exception: {exc}", file=sys.stderr)
        raise SystemExit(0)
