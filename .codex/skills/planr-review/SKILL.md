---
name: planr-review
description: Review completed Planr work against the plan, git diff, and verification output using path-scoped evidence.
source: https://github.com/regenrek/codex-planr/tree/main/.codex/skills/planr-review
license: MIT
---

# Planr Review

Use this skill after implementation to audit whether the actual diff and tests satisfy the plan.

## Review Checklist

1. Compare the plan scope to changed files.
2. Inspect git diff for unplanned or risky edits.
3. Confirm verification commands ran and produced credible output.
4. Identify missing tests, unverified assumptions, or stale status.
5. Return an honest verdict: pass, needs fix, or blocked.
