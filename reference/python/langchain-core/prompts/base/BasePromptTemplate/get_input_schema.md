---
title: "get_input_schema"
description: "Get the input schema for the prompt."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/get_input_schema"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, get_input_schema]
---

# get_input_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/get_input_schema)

Get the input schema for the prompt.

## Signature

```python
get_input_schema(
    self,
    config: RunnableConfig | None = None,
) -> type[BaseModel]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | Configuration for the prompt. (default: `None`) |

## Returns

`type[BaseModel]`

The input schema for the prompt.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/prompts/base.py#L139)
