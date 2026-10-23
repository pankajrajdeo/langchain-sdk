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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/store.py#L601)
