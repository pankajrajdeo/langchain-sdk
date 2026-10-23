---
title: "merge"
description: "Merge two runtimes together."
source: "https://reference.langchain.com/python/langgraph/runtime/Runtime/merge"
category: "reference"
tags: [reference, langgraph, runtime, merge]
---

# merge

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/runtime/Runtime/merge)

Merge two runtimes together.

If a value is not provided in the other runtime, the value from the current runtime is used.

## Signature

```python
merge(
    self,
    other: Runtime[ContextT],
) -> Runtime[ContextT]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/runtime.py#L240)
