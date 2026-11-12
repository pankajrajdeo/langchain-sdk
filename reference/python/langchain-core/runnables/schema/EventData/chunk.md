---
title: "chunk"
description: "A streaming chunk from the output that generated the event."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/chunk"
category: "reference"
tags: [reference, langchain-core, runnables, schema, eventdata, chunk]
---

# chunk

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/chunk)

A streaming chunk from the output that generated the event.

chunks support addition in general, and adding them up should result
in the output of the `Runnable` that generated the event.

## Signature

```python
chunk: Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/runnables/schema.py#L42)
