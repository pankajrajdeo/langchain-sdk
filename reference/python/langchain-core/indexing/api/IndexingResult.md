---
title: "IndexingResult"
description: "Return a detailed a breakdown of the result of the indexing operation."
source: "https://reference.langchain.com/python/langchain-core/indexing/api/IndexingResult"
category: "reference"
tags: [reference, langchain-core, indexing, api, indexingresult]
---

# IndexingResult

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/api/IndexingResult)

Return a detailed a breakdown of the result of the indexing operation.

## Signature

```python
IndexingResult()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    num_added: int,
    num_updated: int,
    num_deleted: int,
    num_skipped: int,
)
```

| Name | Type |
|------|------|
| `num_added` | `int` |
| `num_updated` | `int` |
| `num_deleted` | `int` |
| `num_skipped` | `int` |

## Properties

- `num_added`
- `num_updated`
- `num_deleted`
- `num_skipped`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/indexing/api.py#L283)
