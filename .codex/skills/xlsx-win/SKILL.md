---
name: xlsx-win
description: Windows Microsoft Excel automation for .xlsx files using Microsoft 365 desktop COM workflows and Python helpers.
source: https://github.com/dachent/skills/tree/main/xlsx-win
---

# Xlsx Win

Use this skill when the user needs to inspect, edit, create, calculate, export, or QA Excel workbooks on Windows with local Microsoft Excel desktop automation.

## Rules

1. Prefer Excel COM automation when a signed-in desktop session and Microsoft Excel are available.
2. Run shared Office COM preflight before COM work.
3. Preserve formulas, styles, charts, pivots, worksheets, named ranges, and macros unless asked otherwise.
4. Save edited workbooks to a new path unless explicitly asked for in-place edits.
5. Reopen, calculate, and validate outputs before declaring success.
