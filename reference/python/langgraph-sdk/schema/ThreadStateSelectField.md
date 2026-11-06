---
title: "ThreadStateSelectField"
description: "Type Alias in langgraph_sdk"
source: "https://reference.langchain.com/python/langgraph-sdk/schema/ThreadStateSelectField"
category: "reference"
tags: [reference, langgraph-sdk, schema, threadstateselectfield]
---

# ThreadStateSelectField

> **Type Alias** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/ThreadStateSelectField)

Also accepts `values.<key>` for a single state key, e.g. `values.messages`.

## Signature

```python
ThreadStateSelectField = Literal['values', 'next', 'tasks', 'checkpoint', 'metadata', 'created_at', 'parent_checkpoint', 'interrupts'] | str
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5847733bcb186c26b32da5cc822eaf8a89deffeb/libs/sdk-py/langgraph_sdk/schema.py#L489)
