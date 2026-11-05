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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/schema.py#L485)
