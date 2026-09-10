---
title: "mode"
description: "Effect when a tool call matches this rule:"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemPermission/mode"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystempermission, mode]
---

# mode

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemPermission/mode)

Effect when a tool call matches this rule:

- `"allow"` (default): the call proceeds.
- `"deny"`: the tool returns a permission-denied error.
- `"interrupt"`: the call is paused for human approval via
    [`HumanInTheLoopMiddleware`][langchain.agents.middleware.HumanInTheLoopMiddleware].

    Best paired with patterns that have a literal leading anchor (e.g.,
    `/secrets/**`, `/projects/*/secrets/**`). Bulk tools
    (`ls`/`glob`/`grep`) fire the interrupt based on whether their
    search subtree could overlap the rule's anchored prefix, so a fully
    unanchored pattern (`/**/secrets`) collapses to `/` and
    conservatively over-fires for any bulk call.

## Signature

```python
mode: Literal['allow', 'deny', 'interrupt'] = 'allow'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/filesystem.py#L392)
