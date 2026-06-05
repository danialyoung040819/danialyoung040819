---
name: research-paper-writing
description: Improve academic paper writing quality for ML/CV/NLP-style papers with clear section structure, paragraph flow, and reviewer-facing presentation. Use when drafting or revising Abstract, Introduction, Related Work, Method, Experiments, or Conclusion; polishing figures/tables; checking claim-support alignment; or performing self-review before submission.
source: https://github.com/Master-cai/Research-Paper-Writing-Skills/tree/main/research-paper-writing
license: MIT
---

# Research Paper Writing

## Overview

Use this skill to rewrite a research paper into a reviewer-friendly, high-clarity draft. Prioritize first-impression quality (figures/tables/layout), logical flow, and evidence-backed claims.

## Core Workflow

1. Clarify the paper story before sentence-level edits.
2. Use section-specific guidance in `references/` when it exists.
3. Rewrite paragraph-by-paragraph with one message per paragraph.
4. Run reverse outlining after writing each section.
5. Check every major claim in Abstract/Introduction against experimental evidence.
6. Run final-paper adversarial review before submission.

## Global Principles

1. Keep one paragraph for one message only.
2. State the paragraph message in the first sentence.
3. Make nouns self-contained; define new terms before reusing them.
4. Maintain sentence-to-sentence flow through cause, contrast, consequence, or refinement.
5. Iterate with adversarial self-review: read as a skeptical reviewer.
6. Treat visual quality as core content, not decoration.
7. Use clean teaser/pipeline figures and readable, minimal-ink tables.
8. Keep formatting consistent and tidy.

## Paragraph Clarity Check

When evaluating whether a paragraph flows:

1. Read as an external reviewer and ask whether it has one explicit message, a clear first-sentence topic, readable terms, and sentence-to-sentence logic.
2. Reverse-outline the section: thesis, paragraph topic sentences, and evidence under each paragraph.
3. Remove or rewrite paragraphs that do not map cleanly to the section thesis.
4. Use temporary headers or transitions to diagnose flow, then remove anything unnecessary.

## Section Guides

Load only the needed section guide/reference for the current edit target:

- Introduction
- Abstract
- Related Work
- Method
- Experiments
- Conclusion
- Paper review
- Paragraph clarity source
- Example bank

## Paper Review Core Points

1. Add and answer an end-of-draft self-review list in five dimensions: contribution, writing clarity, experimental strength, evaluation completeness, and method design soundness.
2. Treat claim-evidence alignment as a hard constraint, especially for Abstract and Introduction.
3. Review as a skeptical reviewer and resolve high-risk questions.
4. Revise until major rejection risks are explicitly addressed.

## Execution Rules

1. Build a mini-outline before drafting prose.
2. For each subsection, include motivation, design, and technical advantage when applicable.
3. Avoid a style that looks like incremental patching of a naive baseline.
4. Keep terminology stable across the full paper.
5. If a claim cannot be supported by results, weaken or remove it.
6. Before finalizing, append and answer a five-dimension self-review checklist, then revise unresolved items.
7. Do not load all section references at once; load only the specific guide needed.

## Output Contract

When asked to rewrite or draft sections, return:

1. A compact section outline (3-7 bullets).
2. Revised paragraphs with explicit paragraph roles.
3. A short self-review checklist for clarity, flow, terminology consistency, unsupported claims, and missing evidence.
4. A claim-evidence map for major claims using `Claim: ... | Evidence: ... | Status: supported/needs evidence`.
