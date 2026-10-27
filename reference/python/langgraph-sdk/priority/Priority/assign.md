---
title: "assign"
description: "Register the function that assigns a thread's priority settings."
source: "https://reference.langchain.com/python/langgraph-sdk/priority/Priority/assign"
category: "reference"
tags: [reference, langgraph-sdk, priority, assign]
---

# assign

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/priority/Priority/assign)

Register the function that assigns a thread's priority settings.

The function receives a `PriorityContext` and returns `PrioritySettings`,
or `None` for the defaults.

## Signature

```python
assign(
    self,
    fn: _AssignHandlerT,
) -> _AssignHandlerT
```

## Description

**Example:**

```python
@priority.assign
async def assign(ctx: PriorityContext) -> PrioritySettings | None:
    if ctx.cron_id is not None:
        return {"priority": -2}
    return None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `fn` | `_AssignHandlerT` | Yes | The assign handler function |

## Returns

`_AssignHandlerT`

The registered handler function

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/priority/__init__.py#L126)
