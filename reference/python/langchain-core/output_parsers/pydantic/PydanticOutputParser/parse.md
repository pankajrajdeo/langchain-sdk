---
title: "parse"
description: "Parse the output of an LLM call to a Pydantic object."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/parse"
category: "reference"
tags: [reference, langchain-core, output_parsers, pydantic, pydanticoutputparser, parse]
---

# parse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/parse)

Parse the output of an LLM call to a Pydantic object.

## Signature

```python
parse(
    self,
    text: str,
) -> TBaseModel
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The output of the LLM call. |

## Returns

`TBaseModel`

The parsed Pydantic object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/output_parsers/pydantic.py#L84)
