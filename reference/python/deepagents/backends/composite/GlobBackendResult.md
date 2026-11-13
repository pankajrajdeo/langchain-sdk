---
title: "GlobBackendResult"
description: "Type Alias in deepagents"
source: "https://reference.langchain.com/python/deepagents/backends/composite/GlobBackendResult"
category: "reference"
tags: [reference, deepagents, backends, composite, globbackendresult]
---

# GlobBackendResult

> **Type Alias** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/GlobBackendResult)

Result shape accepted by composite glob merge helpers.

Composite glob supports both current `GlobResult` values and legacy
`list[FileInfo]` backend returns.

## Signature

```python
GlobBackendResult = GlobResult | list[FileInfo]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/backends/composite.py#L144)
