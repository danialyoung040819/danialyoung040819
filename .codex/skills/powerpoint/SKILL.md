---
name: powerpoint
description: Create, edit, analyze, and validate Microsoft PowerPoint presentations and .pptx slide decks with editable layouts, charts, diagrams, images, speaker notes, and templates.
version: 1.0.0
source: https://github.com/anthropics/skills/tree/main/skills/pptx
license: Apache-2.0
aliases: [pptx, slides, presentation]
---

# PowerPoint

Use this skill when the user asks for PowerPoint, PPTX, slide decks, presentations, pitch decks, talks, speaker notes, or editing an existing deck.

## Capabilities

- Create new `.pptx` decks from outlines or source material.
- Edit existing decks while preserving editable objects where possible.
- Add text, images, tables, charts, diagrams, speaker notes, and section dividers.
- Apply brand colors, typography, layouts, and templates.
- Diagnose layout issues such as overflow, overlap, missing fonts, or broken media.

## Recommended Workflow

1. Clarify audience, objective, length, tone, and output path if missing.
2. Create an outline with slide titles and one takeaway per slide.
3. Build editable slides using a native PPTX library such as PptxGenJS or python-pptx.
4. Keep source code or generation notes next to the final deck.
5. Validate the result by inspecting slide count, text overflow, images, and charts.
6. Deliver both the `.pptx` and any source artifacts needed to regenerate it.

## Design Rules

- One main idea per slide.
- Prefer strong hierarchy over dense bullet lists.
- Use consistent margins, spacing, and alignment.
- Keep charts labeled and readable.
- Preserve editability unless the user requests image-only slides.
