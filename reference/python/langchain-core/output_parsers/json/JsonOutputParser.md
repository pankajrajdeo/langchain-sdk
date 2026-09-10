---
title: "JsonOutputParser"
description: "Parse the output of an LLM call to a JSON object."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/json/JsonOutputParser"
category: "reference"
tags: [reference, langchain-core, output_parsers, json, jsonoutputparser]
---

# JsonOutputParser

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/json/JsonOutputParser)

Parse the output of an LLM call to a JSON object.

Probably the most reliable output parser for getting structured data that does *not*
use function calling.

When used in streaming mode, it will yield partial JSON objects containing all the
keys that have been returned so far.

In streaming, if `diff` is set to `True`, yields `JSONPatch` operations describing
the difference between the previous and the current object.

## Signature

```python
JsonOutputParser(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `BaseCumulativeTransformOutputParser[Any]`

## Properties

- `pydantic_object`

## Methods

- [`parse_result()`](https://reference.langchain.com/python/langchain-core/output_parsers/json/JsonOutputParser/parse_result)
- [`parse()`](https://reference.langchain.com/python/langchain-core/output_parsers/json/JsonOutputParser/parse)
- [`get_format_instructions()`](https://reference.langchain.com/python/langchain-core/output_parsers/json/JsonOutputParser/get_format_instructions)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/output_parsers/json.py#L31)
