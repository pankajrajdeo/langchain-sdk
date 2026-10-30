---
title: "parse"
description: "Parse the output of an LLM call to a JSON object."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/JsonOutputFunctionsParser/parse"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_functions, jsonoutputfunctionsparser, parse]
---

# parse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/JsonOutputFunctionsParser/parse)

Parse the output of an LLM call to a JSON object.

## Signature

```python
parse(
    self,
    text: str,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The output of the LLM call. |

## Returns

`Any`

The parsed JSON object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/output_parsers/openai_functions.py#L145)
