---
title: "pydantic_object"
description: "The Pydantic object to use for validation."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/json/JsonOutputParser/pydantic_object"
category: "reference"
tags: [reference, langchain-core, output_parsers, json, jsonoutputparser, pydantic_object]
---

# pydantic_object

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/json/JsonOutputParser/pydantic_object)

The Pydantic object to use for validation.

If `None`, no validation is performed.

## Signature

```python
pydantic_object: Annotated[type[TBaseModel] | None, SkipValidation()] = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/output_parsers/json.py#L44)
