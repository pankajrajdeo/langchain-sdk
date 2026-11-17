---
title: "aglob"
description: "Async version of glob, delegating to aexecute."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aglob"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, aglob]
---

# aglob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aglob)

Async version of `glob`, delegating to `aexecute`.

Bounded by `ASYNC_GLOB_TIMEOUT`: the remote script's own `TIME_BUDGET`
covers only the walk, so without an outer timeout a wedged sandbox
hangs the caller with no upper bound.

## Signature

```python
aglob(
    self,
    pattern: str,
    path: str | None = None,
) -> GlobResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/sandbox.py#L2130)
