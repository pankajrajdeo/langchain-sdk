---
title: "grep"
description: "Search state files for a literal text pattern."
source: "https://reference.langchain.com/python/deepagents/backends/state/StateBackend/grep"
category: "reference"
tags: [reference, deepagents, backends, state, statebackend, grep]
---

# grep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/grep)

Search state files for a literal text pattern.

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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/backends/state.py#L280)
