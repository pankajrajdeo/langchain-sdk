---
title: "gated_coro"
description: "Run a coroutine with a semaphore."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/gated_coro"
category: "reference"
tags: [reference, langchain-core, runnables, utils, gated_coro]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/runnables/utils.py#L50)
