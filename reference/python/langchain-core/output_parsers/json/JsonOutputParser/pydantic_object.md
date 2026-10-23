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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/output_parsers/json.py#L44)
