---
name: docx-win
description: Windows Microsoft Word automation for .docx files using Microsoft 365 desktop COM workflows.
source: https://github.com/dachent/skills/tree/main/docx-win
---

# Docx Win

Use this skill when the user needs to inspect, edit, create, render, export, or QA Microsoft Word documents on Windows with the local Microsoft Word desktop app.

## Rules

1. Prefer Word COM automation when a signed-in desktop session and Microsoft Word are available.
2. Run shared Office COM preflight before COM work.
3. Save edited documents to a new path unless explicitly asked for in-place edits.
4. Preserve tracked changes, comments, styles, fields, and document structure unless asked otherwise.
5. Export or reopen the output for validation before declaring success.
