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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/runtime.py#L296)
