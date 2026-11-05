---
title: "default_init_validator"
description: "Default init validator that blocks jinja2 templates."
source: "https://reference.langchain.com/python/langchain-core/load/load/default_init_validator"
category: "reference"
tags: [reference, langchain-core, load, default_init_validator]
---

# default_init_validator

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/load/default_init_validator)

Default init validator that blocks jinja2 templates.

This is the default validator used by `load()` and `loads()` when no custom
validator is provided.

## Signature

```python
default_init_validator(
    class_path: tuple[str, ...],
    kwargs: dict[str, Any],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `class_path` | `tuple[str, ...]` | Yes | The class path tuple being deserialized. |
| `kwargs` | `dict[str, Any]` | Yes | The kwargs dict for the class constructor. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/load/load.py#L251)
