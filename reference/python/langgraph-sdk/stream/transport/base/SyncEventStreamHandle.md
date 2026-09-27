---
title: "SyncEventStreamHandle"
description: "Handle for one sync filtered event stream."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/transport/base/SyncEventStreamHandle"
category: "reference"
tags: [reference, langgraph-sdk, stream, transport, base, synceventstreamhandle]
---

# SyncEventStreamHandle

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/transport/base/SyncEventStreamHandle)

Handle for one sync filtered event stream.

## Signature

```python
SyncEventStreamHandle(
    self,
    events: Iterator[Event],
    error: Callable[[], BaseException | None],
    close: Callable[[], None],
)
```

## Constructors

```python
__init__(
    self,
    events: Iterator[Event],
    error: Callable[[], BaseException | None],
    close: Callable[[], None],
) -> None
```

| Name | Type |
|------|------|
| `events` | `Iterator[Event]` |
| `error` | `Callable[[], BaseException \| None]` |
| `close` | `Callable[[], None]` |

## Properties

- `events`
- `error`
- `close`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/stream/transport/base.py#L24)
