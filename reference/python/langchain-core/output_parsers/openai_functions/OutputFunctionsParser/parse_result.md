---
title: "parse_result"
description: "Parse the result of an LLM call to a JSON object."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/OutputFunctionsParser/parse_result"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_functions, outputfunctionsparser, parse_result]
---

# parse_result

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/OutputFunctionsParser/parse_result)

Parse the result of an LLM call to a JSON object.

## Signature

```python
parse_result(
    self,
    result: list[Generation],
    *,
    partial: bool = False,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `result` | `list[Generation]` | Yes | The result of the LLM call. |
| `partial` | `bool` | No | Whether to parse partial JSON objects. (default: `False`) |

## Returns

`Any`

The parsed JSON object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/output_parsers/openai_functions.py#L28)
