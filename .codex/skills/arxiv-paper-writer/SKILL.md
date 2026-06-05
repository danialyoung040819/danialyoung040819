---
name: arxiv-paper-writer
description: Write LaTeX ML/AI review articles for arXiv using the IEEEtran template and verified BibTeX citations.
compatibility: Python 3.8+ for scripts. Web browsing/search for citation verification. LaTeX is required (pdflatex + bibtex or latexmk).
metadata:
  short-description: ML/AI review papers (IEEEtran template) with verified citations
source: https://github.com/renocrypt/latex-arxiv-SKILL/tree/main/.codex/skills/arxiv-paper-writer
---

# ML/AI Review Paper Workflow (IEEEtran template)

## When to Use

- ML/AI review papers for arXiv.
- LaTeX + BibTeX workflows with verified citations.
- Citation validation or repair on existing LaTeX projects.

## When NOT to Use

- Novel experimental research papers.
- Non-academic documents.

## Inputs

- Topic description (required).
- Constraints such as venue, page limit, author, or affiliation (optional).
- Existing project path for citation validation (optional).

## Outputs

- `main.tex`
- `ref.bib`
- `IEEEtran.cls`
- `plan/*.md`
- `issues/*.csv`
- figures/tables and compiled `main.pdf`
- optional `notes/literature-notes.md`
- optional `notes/arxiv-registry.sqlite3`

## Conventions

Run helper scripts from this skill folder when the upstream scripts are installed. The paper/project root contains `main.tex`, `ref.bib`, `plan/`, `issues/`, and `notes/`. For arXiv discovery, metadata, and BibTeX, prefer the upstream `scripts/arxiv_registry.py` helper over ad-hoc metadata scraping.

## Gated Workflow

1. Clarify the review topic, scope, target audience, and constraints.
2. Search arXiv and other official paper sources for candidate citations.
3. Generate a plan file and wait for explicit user approval when the user expects a multi-step paper build.
4. Convert the plan into issue-sized writing tasks.
5. Draft sections with verified citations only.
6. Compile, validate references, and repair citation or LaTeX issues.
7. Run final QA on structure, references, page limits, and PDF output.

## Citation Rules

- Never invent BibTeX.
- Prefer arXiv IDs, DOI records, or publisher pages for metadata.
- Keep BibTeX keys stable after first use.
- Remove uncited bibliography entries before final output.
- Mark uncertain references as needing verification instead of silently proceeding.
