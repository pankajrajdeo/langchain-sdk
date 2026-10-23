---
title: "response_schema"
description: "Schema for the value expected when resuming this interrupt, if the graph provided one."
source: "https://reference.langchain.com/python/langgraph/types/Interrupt/response_schema"
category: "reference"
tags: [reference, langgraph, types, interrupt, response_schema]
---

# response_schema

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/Interrupt/response_schema)

Schema for the value expected when resuming this interrupt, if the graph provided one.

A surfaced interrupt carries JSON Schema (a `dict`); `type[ResponseT]` records the
Python type at construction so `Interrupt[Decision]` is meaningful to type checkers.

## Signature

```python
response_schema: type[ResponseT] | dict[str, Any] | None = response_schema
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/types.py#L623)
