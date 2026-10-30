---
title: "ParsedDataUri"
description: "- TypedDict"
source: "https://reference.langchain.com/python/langchain-core/language_models/_utils/ParsedDataUri"
category: "reference"
tags: [reference, langchain-core, language_models, utils, parseddatauri]
---

# ParsedDataUri

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/_utils/ParsedDataUri)

## Signature

```python
ParsedDataUri()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    source_type: Literal['base64'],
    data: str,
    mime_type: str,
)
```

| Name | Type |
|------|------|
| `source_type` | `Literal['base64']` |
| `data` | `str` |
| `mime_type` | `str` |

## Properties

- `source_type`
- `data`
- `mime_type`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/language_models/_utils.py#L99)
