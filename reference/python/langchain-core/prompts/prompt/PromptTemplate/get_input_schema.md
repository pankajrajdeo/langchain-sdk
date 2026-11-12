---
title: "get_input_schema"
description: "Get the input schema for the prompt."
source: "https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/get_input_schema"
category: "reference"
tags: [reference, langchain-core, prompts, prompt, prompttemplate, get_input_schema]
---

# get_input_schema

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/prompt/PromptTemplate/get_input_schema)

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
| `config` | `RunnableConfig \| None` | No | The runnable configuration. (default: `None`) |

## Returns

`type[BaseModel]`

The input schema for the prompt.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/prompts/prompt.py#L127)
