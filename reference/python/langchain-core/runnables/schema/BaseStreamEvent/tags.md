---
title: "tags"
description: "Tags associated with the Runnable that generated this event."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent/tags"
category: "reference"
tags: [reference, langchain-core, runnables, schema, basestreamevent, tags]
---

# tags

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/BaseStreamEvent/tags)

Tags associated with the `Runnable` that generated this event.

Tags are always inherited from parent `Runnable` objects.

Tags can either be bound to a `Runnable` using `.with_config({"tags":  ["hello"]})`
or passed at run time using `.astream_events(..., {"tags": ["hello"]})`.

## Signature

```python
tags: NotRequired[list[str]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/schema.py#L130)
