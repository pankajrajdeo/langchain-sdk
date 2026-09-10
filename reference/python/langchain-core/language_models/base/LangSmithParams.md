---
title: "LangSmithParams"
description: "LangSmith parameters for tracing."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/LangSmithParams"
category: "reference"
tags: [reference, langchain-core, language_models, base, langsmithparams]
---

# LangSmithParams

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/LangSmithParams)

LangSmith parameters for tracing.

## Signature

```python
LangSmithParams()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    ls_provider: str,
    ls_model_name: str,
    ls_model_type: Literal['chat', 'llm'],
    ls_temperature: float | None,
    ls_max_tokens: int | None,
    ls_stop: list[str] | None,
    ls_integration: str,
)
```

| Name | Type |
|------|------|
| `ls_provider` | `str` |
| `ls_model_name` | `str` |
| `ls_model_type` | `Literal['chat', 'llm']` |
| `ls_temperature` | `float \| None` |
| `ls_max_tokens` | `int \| None` |
| `ls_stop` | `list[str] \| None` |
| `ls_integration` | `str` |

## Properties

- `ls_provider`
- `ls_model_name`
- `ls_model_type`
- `ls_temperature`
- `ls_max_tokens`
- `ls_stop`
- `ls_integration`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/base.py#L43)
