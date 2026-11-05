---
title: "gated_coro"
description: "Run a coroutine with a semaphore."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/gated_coro"
category: "reference"
tags: [reference, langchain-core, runnables, base, gated_coro]
---

# gated_coro

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/gated_coro)

Run a coroutine with a semaphore.

## Signature

```python
gated_coro(
    semaphore: asyncio.Semaphore,
    coro: Coroutine[Any, Any, Any],
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `semaphore` | `asyncio.Semaphore` | Yes | The semaphore to use. |
| `coro` | `Coroutine[Any, Any, Any]` | Yes | The coroutine to run. |

## Returns

`Any`

The result of the coroutine.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/runnables/utils.py#L50)
