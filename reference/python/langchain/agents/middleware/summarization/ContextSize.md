---
title: "ContextSize"
description: "Type Alias in langchain"
source: "https://reference.langchain.com/python/langchain/agents/middleware/summarization/ContextSize"
category: "reference"
tags: [reference, langchain, agents, middleware, summarization, contextsize]
---

# ContextSize

> **Type Alias** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/summarization/ContextSize)

Union type for context size specifications.

Can be either:

- [`ContextFraction`][langchain.agents.middleware.summarization.ContextFraction]: A
    fraction of the model's maximum input tokens.
- [`ContextTokens`][langchain.agents.middleware.summarization.ContextTokens]: An absolute
    number of tokens.
- [`ContextMessages`][langchain.agents.middleware.summarization.ContextMessages]: An
    absolute number of messages.

Depending on use with `trigger` or `keep` parameters, this type indicates either
when to trigger summarization or how much context to retain.

## Signature

```python
ContextSize = ContextFraction | ContextTokens | ContextMessages
```

## Description

**Example:**

```python
# ContextFraction
context_size: ContextSize = ("fraction", 0.5)

# ContextTokens
context_size: ContextSize = ("tokens", 3000)

# ContextMessages
context_size: ContextSize = ("messages", 50)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/summarization.py#L189)
