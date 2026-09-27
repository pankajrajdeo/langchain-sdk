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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/exceptions.py#L123)
