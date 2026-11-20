---
title: "error"
description: "The error that occurred during the execution of the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/error"
category: "reference"
tags: [reference, langchain-core, runnables, schema, eventdata, error]
---

# error

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/error)

The error that occurred during the execution of the `Runnable`.

This field is only available if the `Runnable` raised an exception.

!!! version-added "Added in `langchain-core` 1.0.0"

## Signature

```python
error: NotRequired[BaseException]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/runnables/schema.py#L26)
