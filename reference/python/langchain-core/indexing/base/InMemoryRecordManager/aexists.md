---
title: "aexists"
description: "Async check if the provided keys exist in the database."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/aexists"
category: "reference"
tags: [reference, langchain-core, indexing, base, inmemoryrecordmanager, aexists]
---

# aexists

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/InMemoryRecordManager/aexists)

Async check if the provided keys exist in the database.

## Signature

```python
aexists(
    self,
    keys: Sequence[str],
) -> list[bool]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | `Sequence[str]` | Yes | A list of keys to check. |

## Returns

`list[bool]`

A list of boolean values indicating the existence of each key.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/1a41b51b0295d7cc6df45cdede199b4a34649b1d/libs/core/langchain_core/indexing/base.py#L341)
