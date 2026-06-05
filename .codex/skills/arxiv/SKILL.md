---
name: arxiv
description: Search and retrieve academic papers from arXiv by keyword, author, category, or ID; generate stable arXiv links and BibTeX-ready metadata for literature review tasks.
version: 1.0.0
source: https://github.com/NousResearch/hermes-agent/tree/main/skills/research/arxiv
license: MIT
---

# arXiv Research

Use this skill when a task asks for arXiv papers, preprints, paper metadata, abstracts, PDFs, related work, BibTeX, or literature-review searches.

## Workflow

1. Search arXiv with the public Atom API.
2. Prefer exact paper IDs when the user provides them.
3. Preserve version suffixes (`v1`, `v2`, etc.) when citing a version you actually read.
4. Use abstracts first for triage, then PDFs only for papers that matter.
5. Mark unverifiable citations as `[CITATION NEEDED]` rather than inventing metadata.

## Commands

```bash
# Keyword search
curl -s "https://export.arxiv.org/api/query?search_query=all:transformer+attention&max_results=5"

# Latest papers in a category
curl -s "https://export.arxiv.org/api/query?search_query=cat:cs.AI&sortBy=submittedDate&sortOrder=descending&max_results=10"

# Fetch a specific paper
curl -s "https://export.arxiv.org/api/query?id_list=1706.03762"
```

## Query Syntax

- `all:` searches all fields.
- `ti:` searches titles.
- `au:` searches authors.
- `abs:` searches abstracts.
- `cat:` searches categories such as `cs.AI`, `cs.CL`, `cs.CV`, `cs.LG`, or `stat.ML`.

## Output Standards

When reporting results, include title, authors, year/date, arXiv ID, abstract summary, PDF link, and why the paper is relevant to the user's topic.
