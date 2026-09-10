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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/prompts/base.py#L139)
