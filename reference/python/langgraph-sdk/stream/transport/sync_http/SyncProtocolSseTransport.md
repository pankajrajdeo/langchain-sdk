---
title: "SyncProtocolSseTransport"
description: "Sync v3 protocol transport bound to one thread id."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_http/SyncProtocolSseTransport"
category: "reference"
tags: [reference, langgraph-sdk, stream, transport, sync_http, syncprotocolssetransport]
---

# SyncProtocolSseTransport

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_http/SyncProtocolSseTransport)

Sync v3 protocol transport bound to one thread id.

## Signature

```python
SyncProtocolSseTransport(
    self,
    *,
    client: httpx.Client,
    thread_id: str,
    commands_path: str | None = None,
    stream_path: str | None = None,
    headers: Mapping[str, str] | None = None,
)
```

## Constructors

```python
__init__(
    self,
    *,
    client: httpx.Client,
    thread_id: str,
    commands_path: str | None = None,
    stream_path: str | None = None,
    headers: Mapping[str, str] | None = None,
) -> None
```

| Name | Type |
|------|------|
| `client` | `httpx.Client` |
| `thread_id` | `str` |
| `commands_path` | `str \| None` |
| `stream_path` | `str \| None` |
| `headers` | `Mapping[str, str] \| None` |

## Properties

- `thread_id`

## Methods

- [`send_command()`](https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_http/SyncProtocolSseTransport/send_command)
- [`open_event_stream()`](https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_http/SyncProtocolSseTransport/open_event_stream)
- [`close()`](https://reference.langchain.com/python/langgraph-sdk/stream/transport/sync_http/SyncProtocolSseTransport/close)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/stream/transport/sync_http.py#L21)
