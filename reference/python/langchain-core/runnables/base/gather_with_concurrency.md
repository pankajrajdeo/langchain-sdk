---
title: "gather_with_concurrency"
description: "Gather coroutines with a limit on the number of concurrent coroutines."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/gather_with_concurrency"
category: "reference"
tags: [reference, langchain-core, runnables, base, gather_with_concurrency]
---

# gather_with_concurrency

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/gather_with_concurrency)

Gather coroutines with a limit on the number of concurrent coroutines.

## Signature

```python
gather_with_concurrency(
    n: int | None,
    *coros: Coroutine[Any, Any, Any] = (),
) -> list[Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `n` | `int \| None` | Yes | The number of coroutines to run concurrently. |
| `*coros` | `Coroutine[Any, Any, Any]` | No | The coroutines to run. (default: `()`) |

## Returns

`list[Any]`

The results of the coroutines.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/utils.py#L65)
