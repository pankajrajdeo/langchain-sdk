---
title: "PydanticOutputParser"
description: "Parse an output using a Pydantic model."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser"
category: "reference"
tags: [reference, langchain-core, output_parsers, pydantic, pydanticoutputparser]
---

# PydanticOutputParser

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser)

Parse an output using a Pydantic model.

## Signature

```python
PydanticOutputParser(
    self,
    args: Any = (),
    kwargs: Any = {},
)
```

## Extends

- `JsonOutputParser`
- `Generic[TBaseModel]`

## Properties

- `pydantic_object`
- `OutputType`

## Methods

- [`parse_result()`](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/parse_result)
- [`parse()`](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/parse)
- [`get_format_instructions()`](https://reference.langchain.com/python/langchain-core/output_parsers/pydantic/PydanticOutputParser/get_format_instructions)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/output_parsers/pydantic.py#L19)
