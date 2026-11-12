---
title: "get_parents"
description: "Get the parents of a run."
source: "https://reference.langchain.com/python/langchain-core/tracers/stdout/FunctionCallbackHandler/get_parents"
category: "reference"
tags: [reference, langchain-core, tracers, stdout, functioncallbackhandler, get_parents]
---

# get_parents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/stdout/FunctionCallbackHandler/get_parents)

Get the parents of a run.

## Signature

```python
get_parents(
    self,
    run: Run,
) -> list[Run]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run` | `Run` | Yes | The run to get the parents of. |

## Returns

`list[Run]`

A list of parent runs.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/tracers/stdout.py#L69)
