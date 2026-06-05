# Planr Shared Guidance

Source: https://github.com/regenrek/codex-planr

Planr is a portable repo-local planning and execution workflow for Codex. It keeps scope, live status, and review evidence in the repository instead of chat-state. The workflow is:

1. `$planr-plan` defines scope, ownership, phases, verification, and acceptance criteria.
2. `$planr-fix` implements the work and keeps `.planr/status/current.json` honest.
3. `$planr-review` audits the result against the plan, diff, and tests.

Optional follow-up skills:

- `$planr-status`: smallest honest verdict for the current scope.
- `$planr-summary`: recap changed, working, blocked, or unverified items.
