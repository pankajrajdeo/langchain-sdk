---
title: "parse_partial_json"
description: "Parse a JSON string that may be missing closing braces."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/parse_partial_json"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_functions, parse_partial_json]
---

# parse_partial_json

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/json/parse_partial_json)

Parse a JSON string that may be missing closing braces.

## Signature

```python
parse_partial_json(
    s: str,
    *,
    strict: bool = False,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `s` | `str` | Yes | The JSON string to parse. |
| `strict` | `bool` | No | Whether to use strict parsing. (default: `False`) |

## Returns

`Any`

The parsed JSON object as a Python dictionary.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/utils/json.py#L60)
