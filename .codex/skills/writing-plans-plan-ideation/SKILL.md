---
name: writing-plans-plan-ideation
description: Create structured implementation plans from ideation through execution: clarify goals, compare approaches, produce bite-sized tasks, file paths, code examples, verification steps, and checkpoints.
version: 1.0.0
source: https://github.com/obra/superpowers/tree/main
license: MIT
aliases: [writing-plans, plan, ideation]
---

# Writing Plans / Plan / Ideation

Use this skill when the user asks to plan, design, ideate, architect, break down a multi-step task, or turn a vague idea into an implementation-ready plan.

## Ideation First

When the request is vague, ask one focused question at a time until you know:

- the goal and user value,
- constraints and non-goals,
- target platform or stack,
- success criteria,
- timeline and risk tolerance.

Then propose two or three approaches with trade-offs and a recommendation.

## Plan Requirements

A good plan must include:

1. Goal and non-goals.
2. Current-state findings with file paths.
3. Architecture or approach.
4. Bite-sized tasks that an agent with no prior context can execute.
5. Exact files to create or edit.
6. Code examples or pseudocode for tricky parts.
7. Verification commands and expected outcomes.
8. Rollback or safety notes for risky changes.

## Task Template

```markdown
### Task N: <short title>

**Files:**
- Create/Edit: `<path>`
- Test: `<path>`

**Steps:**
1. <small, concrete step>
2. <small, concrete step>
3. Run: `<verification command>`
4. Commit: `<suggested commit message>`

**Acceptance:**
- <observable result>
```

## Rules

- Do not implement while still in ideation unless the user explicitly asks you to proceed.
- Keep tasks independently executable where possible.
- Include verification before any claim of completion.
