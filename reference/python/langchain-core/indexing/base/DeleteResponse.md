---
title: "DeleteResponse"
description: "A generic response for delete operation."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/DeleteResponse"
category: "reference"
tags: [reference, langchain-core, indexing, base, deleteresponse]
---

# DeleteResponse

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/DeleteResponse)

A generic response for delete operation.

The fields in this response are optional and whether the `VectorStore`
returns them or not is up to the implementation.

## Signature

```python
DeleteResponse()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    num_deleted: int,
    succeeded: Sequence[str],
    failed: Sequence[str],
    num_failed: int,
)
```

| Name | Type |
|------|------|
| `num_deleted` | `int` |
| `succeeded` | `Sequence[str]` |
| `failed` | `Sequence[str]` |
| `num_failed` | `int` |

## Properties

- `num_deleted`
- `succeeded`
- `failed`
- `num_failed`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/indexing/base.py#L460)
