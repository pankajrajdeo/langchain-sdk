---
title: "create_non_standard_block"
description: "Create a NonStandardContentBlock."
source: "https://reference.langchain.com/python/langchain-core/messages/content/create_non_standard_block"
category: "reference"
tags: [reference, langchain-core, messages, content, create_non_standard_block]
---

# create_non_standard_block

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/content/create_non_standard_block)

Create a `NonStandardContentBlock`.

## Signature

```python
create_non_standard_block(
    value: dict[str, Any],
    *,
    id: str | None = None,
    index: int | str | None = None,
) -> NonStandardContentBlock
```

## Description

!!! note

The `id` is generated automatically if not provided, using a UUID4 format
prefixed with `'lc_'` to indicate it is a LangChain-generated ID.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `value` | `dict[str, Any]` | Yes | Provider-specific content data. |
| `id` | `str \| None` | No | Content block identifier.  Generated automatically if not provided. (default: `None`) |
| `index` | `int \| str \| None` | No | Index of block in aggregate response.  Used during streaming. (default: `None`) |

## Returns

`NonStandardContentBlock`

A properly formatted `NonStandardContentBlock`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/content.py#L1454)
