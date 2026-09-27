---
title: "submit"
description: "Submit a function to the executor."
source: "https://reference.langchain.com/python/langchain-core/runnables/config/ContextThreadPoolExecutor/submit"
category: "reference"
tags: [reference, langchain-core, runnables, config, contextthreadpoolexecutor, submit]
---

# submit

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/ContextThreadPoolExecutor/submit)

Submit a function to the executor.

## Signature

```python
submit(
    self,
    func: Callable[P, T],
    *args: P.args = (),
    **kwargs: P.kwargs = {},
) -> Future[T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `func` | `Callable[P, T]` | Yes | The function to submit. |
| `*args` | `P.args` | No | The positional arguments to the function. (default: `()`) |
| `**kwargs` | `P.kwargs` | No | The keyword arguments to the function. (default: `{}`) |

## Returns

`Future[T]`

The future for the function.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/config.py#L610)
