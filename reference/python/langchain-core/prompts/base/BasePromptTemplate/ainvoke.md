---
title: "ainvoke"
description: "Async invoke the prompt."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/ainvoke"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, ainvoke]
---

# ainvoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/ainvoke)

Async invoke the prompt.

## Signature

```python
ainvoke(
    self,
    input: builtins.dict[str, Any],
    config: RunnableConfig | None = None,
    kwargs: Any = {},
) -> PromptValue
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `builtins.dict[str, Any]` | Yes | Input to the prompt. |
| `config` | `RunnableConfig \| None` | No | Configuration for the prompt. (default: `None`) |

## Returns

`PromptValue`

The output of the prompt.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/prompts/base.py#L238)
