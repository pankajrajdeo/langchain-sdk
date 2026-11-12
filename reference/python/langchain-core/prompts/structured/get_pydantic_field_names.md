---
title: "get_pydantic_field_names"
description: "Get field names, including aliases, for a pydantic class."
source: "https://reference.langchain.com/python/langchain-core/prompts/structured/get_pydantic_field_names"
category: "reference"
tags: [reference, langchain-core, prompts, structured, get_pydantic_field_names]
---

# get_pydantic_field_names

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/get_pydantic_field_names)

Get field names, including aliases, for a pydantic class.

## Signature

```python
get_pydantic_field_names(
    pydantic_cls: Any,
) -> set[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pydantic_cls` | `Any` | Yes | Pydantic class. |

## Returns

`set[str]`

Field names.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/utils/utils.py#L193)
