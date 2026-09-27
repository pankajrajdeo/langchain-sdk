---
title: "try_neq_default"
description: "Try to determine if a value is different from the default."
source: "https://reference.langchain.com/python/langchain-core/load/serializable/try_neq_default"
category: "reference"
tags: [reference, langchain-core, load, serializable, try_neq_default]
---

# try_neq_default

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/serializable/try_neq_default)

Try to determine if a value is different from the default.

## Signature

```python
try_neq_default(
    value: Any,
    key: str,
    model: BaseModel,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `value` | `Any` | Yes | The value. |
| `key` | `str` | Yes | The key. |
| `model` | `BaseModel` | Yes | The Pydantic model. |

## Returns

`bool`

Whether the value is different from the default.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/load/serializable.py#L59)
