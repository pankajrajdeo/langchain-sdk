---
title: "get_function_nonlocals"
description: "Get the values a function reaches from outside its own scope."
source: "https://reference.langchain.com/python/langgraph/pregel/_utils/get_function_nonlocals"
category: "reference"
tags: [reference, langgraph, pregel, utils, get_function_nonlocals]
---

# get_function_nonlocals

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_utils/get_function_nonlocals)

Get the values a function reaches from outside its own scope.

## Signature

```python
get_function_nonlocals(
    func: Callable,
) -> list[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable` | Yes | The function to check. |

## Returns

`list[Any]`

Every captured cell value, the globals the function names, and each

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_utils.py#L161)
