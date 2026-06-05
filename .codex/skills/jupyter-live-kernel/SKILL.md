---
name: jupyter-live-kernel
description: "Iterative Python via live Jupyter kernel (hamelnb)."
version: 1.0.0
author: Hermes Agent
license: MIT
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [jupyter, notebook, repl, data-science, exploration, iterative]
    category: data-science
source: https://github.com/NousResearch/hermes-agent/tree/main/skills/data-science/jupyter-live-kernel
---

# Jupyter Live Kernel (hamelnb)

Gives you a stateful Python REPL via a live Jupyter kernel. Variables persist across executions. Use this instead of one-shot scripts when you need to build up state incrementally, explore APIs, inspect DataFrames, or iterate on complex code.

## When to Use

- Iterative exploration.
- State across steps.
- Data science and ML experiments.
- Notebook-like workflows.

Rule of thumb: if you would want a Jupyter notebook for the task, use this skill.

## Prerequisites

1. `uv` must be installed (`which uv`).
2. JupyterLab must be installed (`uv tool install jupyterlab`).
3. A Jupyter server must be running.

## Setup

The upstream hamelnb script path is:

```bash
SCRIPT="$HOME/.agent-skills/hamelnb/skills/jupyter-live-kernel/scripts/jupyter_live_kernel.py"
```

If not cloned yet:

```bash
git clone https://github.com/hamelsmu/hamelnb.git ~/.agent-skills/hamelnb
```

Start JupyterLab when needed:

```bash
jupyter-lab --no-browser --port=8888 --notebook-dir=$HOME/notebooks \
  --IdentityProvider.token='' --ServerApp.password='' > /tmp/jupyter.log 2>&1 &
```

## Core Workflow

Always use `--compact` when the upstream script supports it.

```bash
uv run "$SCRIPT" servers --compact
uv run "$SCRIPT" notebooks --compact
uv run "$SCRIPT" execute --path scratch.ipynb --code 'print("hello")' --compact
uv run "$SCRIPT" variables --path scratch.ipynb list --compact
uv run "$SCRIPT" restart-run-all --path scratch.ipynb --save-outputs --compact
```

## Practical Tips

- First execution after server start may timeout; retry once.
- The kernel Python is JupyterLab's Python, so install packages there.
- For pure REPL use, create `scratch.ipynb` and repeatedly call `execute`.
- Argument order matters: subcommand flags like `--path` go before nested actions.
- For long-running operations, pass a larger timeout such as `--timeout 120`.
