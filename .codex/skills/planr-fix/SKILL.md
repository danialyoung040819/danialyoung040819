---
name: planr-fix
description: Execute an approved Planr scope while keeping implementation status honest and verification evidence current.
source: https://github.com/regenrek/codex-planr/tree/main/.codex/skills/planr-fix
license: MIT
---

# Planr Fix

Use this skill to implement work from an approved Planr plan.

## Rules

1. Work only within the planned scope unless explicitly approved.
2. Keep `.planr/status/current.json` honest when the full scaffold exists.
3. Prefer direct fixes over compatibility shims or quiet fallbacks.
4. Run planned verification commands and record evidence.
5. Do not mark work complete while tests are missing, blocked, or failing.
