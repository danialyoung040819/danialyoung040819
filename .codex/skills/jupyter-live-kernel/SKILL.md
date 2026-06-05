---
name: jupyter-live-kernel
description: Use a live Jupyter kernel for stateful, iterative Python execution, notebooks, data exploration, ML experimentation, and inspecting intermediate results.
version: 1.0.0
source: https://github.com/NousResearch/hermes-agent/tree/main/skills/data-science/jupyter-live-kernel
license: MIT
---

# Jupyter Live Kernel

Use this skill when the user needs notebook-style, stateful Python work: exploratory data analysis, iterative plotting, API exploration, ML experiments, or debugging values across multiple executions.

## When to Prefer This

- Variables need to persist between runs.
- You need to inspect intermediate DataFrames, arrays, plots, or model outputs.
- The work would naturally happen in a notebook instead of a one-shot script.

## Setup Pattern

```bash
# Check for uv and Jupyter
which uv
uv tool list | sed -n '/jupyter/p'

# Start JupyterLab if needed
jupyter-lab --no-browser --port=8888 --notebook-dir="$HOME/notebooks" \
  --IdentityProvider.token='' --ServerApp.password='' > /tmp/jupyter.log 2>&1 &
```

## Operating Rules

1. Keep scratch notebooks in a task-local or user-approved notebooks directory.
2. Use compact output where supported to avoid excessive logs.
3. Retry once after initial kernel/session timeouts.
4. Save important plots, tables, and notebooks as artifacts.
5. For clean verification, restart the kernel and run all cells top-to-bottom.
