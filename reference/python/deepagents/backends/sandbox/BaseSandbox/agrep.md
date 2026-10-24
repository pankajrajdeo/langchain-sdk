---
title: "agrep"
description: "Async version of grep, delegating to aexecute with timeout guard."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/agrep"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, agrep]
---

# agrep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/agrep)

Async version of `grep`, delegating to `aexecute` with timeout guard.

## Signature

```python
agrep(
    self,
    pattern: str,
    path: str | None = None,
    glob: str | None = None,
    *,
    max_count: int | None = None,
) -> GrepResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/sandbox.py#L2093)
