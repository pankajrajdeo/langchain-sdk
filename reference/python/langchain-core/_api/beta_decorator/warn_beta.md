---
title: "warn_beta"
description: "Display a standardized beta annotation."
source: "https://reference.langchain.com/python/langchain-core/_api/beta_decorator/warn_beta"
category: "reference"
tags: [reference, langchain-core, api, beta_decorator, warn_beta]
---

# warn_beta

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/beta_decorator/warn_beta)

Display a standardized beta annotation.

## Signature

```python
warn_beta(
    *,
    message: str = '',
    name: str = '',
    obj_type: str = '',
    addendum: str = '',
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `str` | No | Override the default beta message.  The %(name)s, %(obj_type)s, %(addendum)s format specifiers will be replaced by the values of the respective arguments passed to this function. (default: `''`) |
| `name` | `str` | No | The name of the annotated object. (default: `''`) |
| `obj_type` | `str` | No | The object type being annotated. (default: `''`) |
| `addendum` | `str` | No | Additional text appended directly to the final message. (default: `''`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/_api/beta_decorator.py#L226)
