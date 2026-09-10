---
title: "get_lambda_source"
description: "Get the source code of a lambda function."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/get_lambda_source"
category: "reference"
tags: [reference, langchain-core, runnables, base, get_lambda_source]
---

# get_lambda_source

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/get_lambda_source)

Get the source code of a lambda function.

## Signature

```python
get_lambda_source(
    func: Callable[..., Any],
) -> str | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[..., Any]` | Yes | a Callable that can be a lambda function. |

## Returns

`str | None`

the source code of the lambda function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/utils.py#L387)
