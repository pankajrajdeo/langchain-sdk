---
title: "Summarizer"
description: "Type Alias in langchain"
source: "https://reference.langchain.com/python/langchain/agents/middleware/summarization/Summarizer"
category: "reference"
tags: [reference, langchain, agents, middleware, summarization, summarizer]
---

# Summarizer

> **Type Alias** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/summarization/Summarizer)

Generates a summary from the messages selected for summarization.

Either a chat model (or model string) prompted with the summary prompt, or a
`Runnable` or callable taking the messages and returning the summary text.

## Signature

```python
Summarizer = str | BaseChatModel | Runnable[list[AnyMessage], str] | Callable[[list[AnyMessage]], str] | Callable[[list[AnyMessage]], Coroutine[Any, Any, str]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/summarization.py#L42)
