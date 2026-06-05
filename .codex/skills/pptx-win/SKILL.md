---
name: pptx-win
description: Windows PowerPoint automation for .pptx files in Codex or other local Windows environments with Microsoft 365 installed. Use when opening, inspecting, editing, creating, rendering, exporting, or QAing PowerPoint presentations on Windows.
source: https://github.com/dachent/skills/tree/main/pptx-win
---

# Pptx Win

Prefer this skill over LibreOffice-based flows when PowerPoint desktop is available. Use native Microsoft PowerPoint COM automation first, but only after helper preflight confirms the current shell is the signed-in desktop user session.

## Preflight

```powershell
& "$env:USERPROFILE\.codex\skills\.shared\office-com\scripts\office_com_preflight.ps1" -Apps PowerPoint
```

If preflight reports `can_use_com = false`, do not create `PowerPoint.Application` from the Codex sandbox. Prepare inputs in Codex, then run COM steps from a regular PowerShell window opened as the signed-in desktop user.

## Workflow Decision Tree

1. Smoke test: `powershell -ExecutionPolicy Bypass -File scripts/smoke_test.ps1`.
2. Inspect a deck with `scripts/presentation_report.ps1` and `scripts/export_slides.ps1`.
3. Replace placeholders with `scripts/replace_text.ps1` and a JSON mapping.
4. For custom layout changes, write a task-specific PowerShell script importing `scripts/pptx_com.psm1`.
5. Use OOXML fallback utilities only when COM automation is insufficient.

## Operating Rules

- Save edited output to a new path unless in-place edits are explicitly requested.
- Close presentations and quit PowerPoint in `finally` blocks.
- Never call `New-Object -ComObject PowerPoint.Application` directly from a sandbox.
- Export slide images after material changes and inspect them before declaring success.
- Keep speaker notes and comments unless the user asks to remove them.
