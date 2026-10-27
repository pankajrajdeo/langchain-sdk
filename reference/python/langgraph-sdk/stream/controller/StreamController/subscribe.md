---
title: "subscribe"
description: "Open a typed subscription against the shared SSE."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/controller/StreamController/subscribe"
category: "reference"
tags: [reference, langgraph-sdk, stream, controller, streamcontroller, subscribe]
---

# subscribe

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/controller/StreamController/subscribe)

Open a typed subscription against the shared SSE.

Returns an async iterator that yields raw `Event` dicts matching the
given filter. Multiple concurrent subscribes share one HTTP connection
whose union expands or rotates as subscriptions come and go.

## Signature

```python
subscribe(
    self,
    channels: list[str],
    *,
    namespaces: list[list[str]] | None = None,
    depth: int | None = None,
) -> AsyncIterator[Event]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/stream/controller.py#L144)
