---
title: "EventStreamHandle"
description: "Handle for one async filtered event stream."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/transport/base/EventStreamHandle"
category: "reference"
tags: [reference, langgraph-sdk, stream, transport, base, eventstreamhandle]
---

# EventStreamHandle

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/transport/base/EventStreamHandle)

Handle for one async filtered event stream.

## Signature

```python
EventStreamHandle(
    self,
    events: AsyncIterator[Event],
    ready: asyncio.Future[None],
    done: asyncio.Future[BaseException | None],
    close: Callable[[], Awaitable[None]],
)
```

## Constructors

```python
__init__(
    self,
    events: AsyncIterator[Event],
    ready: asyncio.Future[None],
    done: asyncio.Future[BaseException | None],
    close: Callable[[], Awaitable[None]],
) -> None
```

| Name | Type |
|------|------|
| `events` | `AsyncIterator[Event]` |
| `ready` | `asyncio.Future[None]` |
| `done` | `asyncio.Future[BaseException \| None]` |
| `close` | `Callable[[], Awaitable[None]]` |

## Properties

- `events`
- `ready`
- `done`
- `close`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/stream/transport/base.py#L14)
