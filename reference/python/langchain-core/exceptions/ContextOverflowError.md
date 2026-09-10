---
title: "ContextOverflowError"
description: "Exception raised when input exceeds the model's context limit."
source: "https://reference.langchain.com/python/langchain-core/exceptions/ContextOverflowError"
category: "reference"
tags: [reference, langchain-core, exceptions, contextoverflowerror]
---

# ContextOverflowError

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/exceptions/ContextOverflowError)

Exception raised when input exceeds the model's context limit.

This exception is raised by chat models when the input tokens exceed
the maximum context window supported by the model.

## Signature

```python
ContextOverflowError()
```

## Extends

- `ModelError`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/exceptions.py#L123)
