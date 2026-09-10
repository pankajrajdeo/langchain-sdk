---
title: "AsyncProjection"
description: "Async iterable of deltas that is also awaitable for the final value."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection"
category: "reference"
tags: [reference, langchain-core, language_models, chat_model_stream, asyncprojection]
---

# AsyncProjection

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection)

Async iterable of deltas that is also awaitable for the final value.

Uses an `asyncio.Event` to notify consumers of state changes. Each
waiter — the awaitable (`__await__`) and each async iterator cursor
— shares the event and re-checks its own condition on wake. The event
is cleared before a waiter awaits, so stale "something happened"
signals don't cause spin loops.

This is single-loop only — producers and consumers must share an
event loop. If cross-thread wake is ever required, revert to a
list-of-futures pattern with `call_soon_threadsafe`.

## Signature

```python
AsyncProjection(
    self,
)
```

## Extends

- `_ProjectionBase`

## Constructors

```python
__init__(
    self,
) -> None
```

## Methods

- [`set_start()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection/set_start)
- [`set_arequest_more()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection/set_arequest_more)
- [`push()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection/push)
- [`complete()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection/complete)
- [`fail()`](https://reference.langchain.com/python/langchain-core/language_models/chat_model_stream/AsyncProjection/fail)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/chat_model_stream.py#L344)
