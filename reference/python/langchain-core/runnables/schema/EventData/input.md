---
title: "input"
description: "The input passed to the Runnable that generated the event."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/input"
category: "reference"
tags: [reference, langchain-core, runnables, schema, eventdata, input]
---

# input

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/input)

The input passed to the `Runnable` that generated the event.

Inputs will sometimes be available at the *START* of the `Runnable`, and
sometimes at the *END* of the `Runnable`.

If a `Runnable` is able to stream its inputs, then its input by definition
won't be known until the *END* of the `Runnable` when it has finished streaming
its inputs.

## Signature

```python
input: Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/schema.py#L16)
