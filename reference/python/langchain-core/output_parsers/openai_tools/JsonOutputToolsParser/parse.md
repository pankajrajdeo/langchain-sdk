---
title: "parse"
description: "Parse the output of an LLM call to a list of tool calls."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/JsonOutputToolsParser/parse"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_tools, jsonoutputtoolsparser, parse]
---

# parse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_tools/JsonOutputToolsParser/parse)

Parse the output of an LLM call to a list of tool calls.

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

The parsed tool calls.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/output_parsers/openai_tools.py#L212)
