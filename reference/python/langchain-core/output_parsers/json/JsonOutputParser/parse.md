---
title: "parse"
description: "Parse the output of an LLM call to a JSON object."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/json/JsonOutputParser/parse"
category: "reference"
tags: [reference, langchain-core, output_parsers, json, jsonoutputparser, parse]
---

# parse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/json/JsonOutputParser/parse)

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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/output_parsers/json.py#L93)
