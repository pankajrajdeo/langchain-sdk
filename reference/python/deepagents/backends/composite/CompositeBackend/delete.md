---
title: "delete"
description: "Delete a file, routing to the appropriate backend."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/delete"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, delete]
---

# delete

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/delete)

Delete a file, routing to the appropriate backend.

`CompositeBackend` always advertises delete support (it overrides this
method), so the `delete` tool is never filtered out for it. A
route may still point at a backend that does not implement `delete`;
rather than letting `NotImplementedError` escape to the caller, that
case is converted into a `DeleteResult` error.

## Signature

```python
delete(
    self,
    file_path: str,
) -> DeleteResult
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `file_path` | `str` | Yes | Absolute file path. |

## Returns

`DeleteResult`

`DeleteResult` with the original path on success, or an error

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/composite.py#L778)
