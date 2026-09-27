---
title: "FuturesDict"
description: "- Generic[F, E] - dict[F, PregelExecutableTask | None]"
source: "https://reference.langchain.com/python/langgraph/pregel/_runner/FuturesDict"
category: "reference"
tags: [reference, langgraph, pregel, runner, futuresdict]
---

# FuturesDict

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_runner/FuturesDict)

## Signature

```python
FuturesDict(
    self,
    event: E,
    callback: weakref.ref[Callable[[PregelExecutableTask, BaseException | None], None]],
    should_stop: Callable[[set[F]], bool],
    future_type: type[F],
)
```

## Extends

- `Generic[F, E]`
- `dict[F, PregelExecutableTask | None]`

## Constructors

```python
__init__(
    self,
    event: E,
    callback: weakref.ref[Callable[[PregelExecutableTask, BaseException | None], None]],
    should_stop: Callable[[set[F]], bool],
    future_type: type[F],
) -> None
```

| Name | Type |
|------|------|
| `event` | `E` |
| `callback` | `weakref.ref[Callable[[PregelExecutableTask, BaseException \| None], None]]` |
| `should_stop` | `Callable[[set[F]], bool]` |
| `future_type` | `type[F]` |

## Properties

- `event`
- `callback`
- `should_stop`
- `counter`
- `done`
- `lock`

## Methods

- [`on_done()`](https://reference.langchain.com/python/langgraph/pregel/_runner/FuturesDict/on_done)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_runner.py#L75)
