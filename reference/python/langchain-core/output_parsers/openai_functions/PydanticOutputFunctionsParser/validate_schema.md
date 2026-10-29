---
title: "validate_schema"
description: "Validate the Pydantic schema."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser/validate_schema"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_functions, pydanticoutputfunctionsparser, validate_schema]
---

# validate_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser/validate_schema)

Validate the Pydantic schema.

## Signature

```python
validate_schema(
    cls,
    values: dict[str, Any],
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `values` | `dict[str, Any]` | Yes | The values to validate. |

## Returns

`Any`

The validated values.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/output_parsers/openai_functions.py#L229)
