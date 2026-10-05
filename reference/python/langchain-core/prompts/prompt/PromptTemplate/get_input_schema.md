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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/prompts/prompt.py#L127)
