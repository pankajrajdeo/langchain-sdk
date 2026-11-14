---
title: "get_runtime"
description: "Get the runtime for the current graph run."
source: "https://reference.langchain.com/python/langgraph/runtime/get_runtime"
category: "reference"
tags: [reference, langgraph, runtime, get_runtime]
---

# get_runtime

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/runtime/get_runtime)

Get the runtime for the current graph run.

## Signature

```python
get_runtime(
    context_schema: type[ContextT] | None = None,
) -> Runtime[ContextT]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `context_schema` | `type[ContextT] \| None` | No | Optional schema used for type hinting the return type of the runtime. (default: `None`) |

## Returns

`Runtime[ContextT]`

The runtime for the current graph run.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/runtime.py#L296)
