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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/backends/store.py#L601)
