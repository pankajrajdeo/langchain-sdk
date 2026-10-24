---
title: "RunnableCallable"
description: "A much simpler version of RunnableLambda that requires sync and async functions."
source: "https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableCallable"
category: "reference"
tags: [reference, langgraph, internal, runnable, runnablecallable]
---

# RunnableCallable

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableCallable)

A much simpler version of RunnableLambda that requires sync and async functions.

## Signature

```python
RunnableCallable(
    self,
    func: Callable[..., Any | Runnable] | None,
    afunc: Callable[..., Awaitable[Any | Runnable]] | None = None,
    *,
    name: str | None = None,
    tags: Sequence[str] | None = None,
    trace: bool = True,
    recurse: bool = True,
    explode_args: bool = False,
    kwargs: Any = {},
)
```

## Extends

- `Runnable`

## Constructors

```python
__init__(
    self,
    func: Callable[..., Any | Runnable] | None,
    afunc: Callable[..., Awaitable[Any | Runnable]] | None = None,
    *,
    name: str | None = None,
    tags: Sequence[str] | None = None,
    trace: bool = True,
    recurse: bool = True,
    explode_args: bool = False,
    kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `func` | `Callable[..., Any \| Runnable] \| None` |
| `afunc` | `Callable[..., Awaitable[Any \| Runnable]] \| None` |
| `name` | `str \| None` |
| `tags` | `Sequence[str] \| None` |
| `trace` | `bool` |
| `recurse` | `bool` |
| `explode_args` | `bool` |
| `kwargs` | `Any` |

## Properties

- `name`
- `func`
- `afunc`
- `tags`
- `kwargs`
- `trace`
- `recurse`
- `explode_args`
- `func_accepts`

## Methods

- [`invoke()`](https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableCallable/invoke)
- [`ainvoke()`](https://reference.langchain.com/python/langgraph/_internal/_runnable/RunnableCallable/ainvoke)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/_internal/_runnable.py#L299)
