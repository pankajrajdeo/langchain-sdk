---
title: "bind_apump"
description: "Async counterpart to bind_pump."
source: "https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/bind_apump"
category: "reference"
tags: [reference, langgraph, stream, mux, streammux, bind_apump]
---

# bind_apump

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/bind_apump)

Async counterpart to `bind_pump`.

## Signature

```python
bind_apump(
    self,
    fn: Callable[[], Awaitable[bool]],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/stream/_mux.py#L182)
