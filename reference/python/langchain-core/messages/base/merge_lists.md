---
title: "merge_lists"
description: "Add many lists, handling None."
source: "https://reference.langchain.com/python/langchain-core/messages/base/merge_lists"
category: "reference"
tags: [reference, langchain-core, messages, base, merge_lists]
---

# merge_lists

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/_merge/merge_lists)

Add many lists, handling `None`.

## Signature

```python
merge_lists(
    left: list[Any] | None,
    *others: list[Any] | None = (),
) -> list[Any] | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `left` | `list[Any] \| None` | Yes | The first list to merge. |
| `others` | `list[Any] \| None` | No | The other lists to merge. (default: `()`) |

## Returns

`list[Any] | None`

The merged list.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/_merge.py#L98)
