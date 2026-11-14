---
title: "ls"
description: "List directory contents (non-recursive)."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/ls"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, ls]
---

# ls

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/ls)

List directory contents (non-recursive).

If path matches a route, lists only that backend. If path is `"/"`,
aggregates default backend plus virtual route directories.
Otherwise lists default backend.

## Signature

```python
ls(
    self,
    path: str,
) -> LsResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `path` | `str` | Yes | Absolute directory path starting with `"/"`. |

## Returns

`LsResult`

`LsResult` with directory entries or error.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/backends/composite.py#L300)
