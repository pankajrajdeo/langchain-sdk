---
title: "is_anthropic_chat_model"
description: "Return whether model is a langchain_anthropic chat model."
source: "https://reference.langchain.com/python/deepagents/middleware/memory/is_anthropic_chat_model"
category: "reference"
tags: [reference, deepagents, middleware, memory, is_anthropic_chat_model]
---

# is_anthropic_chat_model

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/_utils/is_anthropic_chat_model)

Return whether `model` is a `langchain_anthropic` chat model.

Reads `sys.modules` rather than importing `langchain_anthropic`: an instance
of `ChatAnthropic` implies its module is loaded, and importing it eagerly
would add the `anthropic` SDK to every `deepagents` import.

## Signature

```python
is_anthropic_chat_model(
    model: object,
) -> TypeGuard[ChatAnthropic]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/middleware/_utils.py#L34)
