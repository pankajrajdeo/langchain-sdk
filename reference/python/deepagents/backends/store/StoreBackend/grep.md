---
title: "grep"
description: "Search store files for a literal text pattern."
source: "https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/grep"
category: "reference"
tags: [reference, deepagents, backends, store, storebackend, grep]
---

# grep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/store/StoreBackend/grep)

Search store files for a literal text pattern.

## Signature

```python
grep(
    self,
    pattern: str,
    path: str | None = None,
    glob: str | None = None,
    *,
    max_count: int | None = None,
) -> GrepResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/backends/store.py#L593)
