---
title: "validate_input_variables"
description: "Validate input variables."
source: "https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/validate_input_variables"
category: "reference"
tags: [reference, langchain-core, prompts, chat, chatprompttemplate, validate_input_variables]
---

# validate_input_variables

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/chat/ChatPromptTemplate/validate_input_variables)

Validate input variables.

If `input_variables` is not set, it will be set to the union of all input
variables in the messages.

## Signature

```python
validate_input_variables(
    cls,
    values: dict[str, Any],
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `values` | `dict[str, Any]` | Yes | values to validate. |

## Returns

`Any`

Validated values.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/prompts/chat.py#L1051)
