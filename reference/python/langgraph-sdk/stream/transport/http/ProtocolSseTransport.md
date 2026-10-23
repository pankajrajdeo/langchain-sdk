---
title: "ProtocolSseTransport"
description: "v3 protocol transport bound to a single thread_id."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/transport/http/ProtocolSseTransport"
category: "reference"
tags: [reference, langgraph-sdk, stream, transport, http, protocolssetransport]
---

# ProtocolSseTransport

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/transport/http/ProtocolSseTransport)

v3 protocol transport bound to a single `thread_id`.

Commands go to `POST /threads/{thread_id}/commands` (JSON in, JSON out).
`open_event_stream` opens filtered SSE streams against
`POST /threads/{thread_id}/stream/events`.

## Signature

```python
ProtocolSseTransport(
    self,
    *,
    client: httpx.AsyncClient,
    thread_id: str,
    commands_path: str | None = None,
    stream_path: str | None = None,
    headers: Mapping[str, str] | None = None,
    max_queue_size: int = 1024,
)
```

## Constructors

```python
__init__(
    self,
    *,
    client: httpx.AsyncClient,
    thread_id: str,
    commands_path: str | None = None,
    stream_path: str | None = None,
    headers: Mapping[str, str] | None = None,
    max_queue_size: int = 1024,
) -> None
```

| Name | Type |
|------|------|
| `client` | `httpx.AsyncClient` |
| `thread_id` | `str` |
| `commands_path` | `str \| None` |
| `stream_path` | `str \| None` |
| `headers` | `Mapping[str, str] \| None` |
| `max_queue_size` | `int` |

## Properties

- `thread_id`

## Methods

- [`send_command()`](https://reference.langchain.com/python/langgraph-sdk/stream/transport/http/ProtocolSseTransport/send_command)
- [`open_event_stream()`](https://reference.langchain.com/python/langgraph-sdk/stream/transport/http/ProtocolSseTransport/open_event_stream)
- [`close()`](https://reference.langchain.com/python/langgraph-sdk/stream/transport/http/ProtocolSseTransport/close)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/stream/transport/http.py#L33)
