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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/sandbox.py#L1899)
