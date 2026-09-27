---
title: "metadata"
description: "Metadata associated with the Runnable that generated this event."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent/metadata"
category: "reference"
tags: [reference, langchain-core, runnables, schema, basestreamevent, metadata]
---

# metadata

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent/metadata)

Metadata associated with the `Runnable` that generated this event.

Metadata can either be bound to a `Runnable` using

    `.with_config({"metadata": { "foo": "bar" }})`

or passed at run time using

    `.astream_events(..., {"metadata": {"foo": "bar"}})`.

## Signature

```python
metadata: NotRequired[dict[str, Any]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/schema.py#L138)
