---
title: "PromptValue"
description: "Base abstract class for inputs to any language model."
source: "https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue"
category: "reference"
tags: [reference, langchain-core, prompt_values, promptvalue]
---

# PromptValue

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue)

Base abstract class for inputs to any language model.

`PromptValues` can be converted to both LLM (pure text-generation) inputs and
chat model inputs.

## Signature

```python
PromptValue(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `Serializable`
- `ABC`

## Methods

- [`is_lc_serializable()`](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue/is_lc_serializable)
- [`get_lc_namespace()`](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue/get_lc_namespace)
- [`to_string()`](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue/to_string)
- [`to_messages()`](https://reference.langchain.com/python/langchain-core/prompt_values/PromptValue/to_messages)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/prompt_values.py#L24)
