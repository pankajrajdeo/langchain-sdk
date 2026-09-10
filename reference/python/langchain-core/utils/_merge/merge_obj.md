---
title: "merge_obj"
description: "Merge two objects."
source: "https://reference.langchain.com/python/langchain-core/utils/_merge/merge_obj"
category: "reference"
tags: [reference, langchain-core, utils, merge, merge_obj]
---

# merge_obj

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/_merge/merge_obj)

Merge two objects.

It handles specific scenarios where a key exists in both dictionaries but has a
value of `None` in `'left'`. In such cases, the method uses the value from `'right'`
for that key in the merged dictionary.

## Signature

```python
merge_obj(
    left: Any,
    right: Any,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `left` | `Any` | Yes | The first object to merge. |
| `right` | `Any` | Yes | The other object to merge. |

## Returns

`Any`

The merged object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/_merge.py#L180)
