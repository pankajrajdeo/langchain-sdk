---
title: "agrep"
description: "Async version of grep."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/agrep"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, agrep]
---

# agrep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/agrep)

Async version of grep.

See `grep()` for detailed documentation on routing behavior and parameters.

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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/backends/composite.py#L551)
