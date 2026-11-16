---
title: "pydantic_schema"
description: "The Pydantic schema to parse the output with."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser/pydantic_schema"
category: "reference"
tags: [reference, langchain-core, output_parsers, openai_functions, pydanticoutputfunctionsparser, pydantic_schema]
---

# pydantic_schema

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/openai_functions/PydanticOutputFunctionsParser/pydantic_schema)

The Pydantic schema to parse the output with.

If multiple schemas are provided, then the function name will be used to
determine which schema to use.

## Signature

```python
pydantic_schema: TypeBaseModel | dict[str, TypeBaseModel]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/output_parsers/openai_functions.py#L222)
