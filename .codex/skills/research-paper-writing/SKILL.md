---
name: research-paper-writing
description: End-to-end workflow for writing ML/AI research papers, from contribution framing and experiments through analysis, LaTeX drafting, self-review, revision, and submission.
version: 1.1.0
source: https://github.com/NousResearch/hermes-agent/tree/main/skills/research/research-paper-writing
license: MIT
---

# Research Paper Writing Pipeline

Use this skill for drafting, revising, or preparing research papers, especially ML/AI papers for venues such as NeurIPS, ICML, ICLR, ACL, AAAI, COLM, workshops, or arXiv.

## Principles

1. Draft concrete text first when enough context exists; flag assumptions instead of stalling.
2. Never hallucinate citations. Fetch metadata programmatically or mark `[CITATION NEEDED]`.
3. Make the paper a story: one contribution, one narrative, evidence matched to claims.
4. Experiments must support explicit claims.
5. Commit meaningful experiment batches, analyses, and draft changes.

## Pipeline

### Phase 0: Project Setup

- Identify the one-sentence contribution.
- Locate existing code, data, results, notes, and `.bib` files.
- Create a TODO plan for literature, experiments, analysis, drafting, review, and submission.

### Phase 1: Literature Review

- Use arXiv, Semantic Scholar, Crossref, and venue proceedings.
- Build a verified bibliography.
- Group related work by claim and contrast, not by chronological summary.

### Phase 2: Experiment Design

- For each paper claim, define the exact table, figure, or metric that would support it.
- Include baselines, ablations, seeds, statistical tests, and failure cases.

### Phase 3: Execution and Monitoring

- Run reproducible commands.
- Capture configs, random seeds, logs, and raw outputs.
- Stop or redirect experiments that no longer support the narrative.

### Phase 4: Analysis

- Produce publication-ready figures and tables.
- Report uncertainty, variance, and meaningful effect sizes.
- Connect every result back to the story.

### Phase 5: Drafting

Recommended order: title, abstract, introduction, methods, experiments, related work, limitations, conclusion.

### Phase 6: Self-Review

Simulate reviewers for novelty, correctness, clarity, significance, reproducibility, and ethics.

### Phase 7: Submission

Check page limits, templates, anonymization, reproducibility checklist, supplementary material, and final PDF compilation.
