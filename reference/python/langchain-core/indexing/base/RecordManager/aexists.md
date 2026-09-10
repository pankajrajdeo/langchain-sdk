---
title: "aexists"
description: "Asynchronously check if the provided keys exist in the database."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/aexists"
category: "reference"
tags: [reference, langchain-core, indexing, base, recordmanager, aexists]
---

# aexists

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/aexists)

Asynchronously check if the provided keys exist in the database.

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/indexing/base.py#L165)
