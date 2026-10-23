---
title: "glob"
description: "Get FileInfo for files matching glob pattern."
source: "https://reference.langchain.com/python/deepagents/backends/state/StateBackend/glob"
category: "reference"
tags: [reference, deepagents, backends, state, statebackend, glob]
---

# glob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/glob)

Get `FileInfo` for files matching glob pattern.

Matching follows the shared backend contract -- see `BackendProtocol.glob`.
A bare pattern is basename-at-any-depth, so `*.py` matches nested files.
A refused pattern is returned as `GlobResult(error=...)`, not raised.

## Signature

```python
glob(
    self,
    pattern: str,
    path: str | None = None,
) -> GlobResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/state.py#L292)
