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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/stream/_mux.py#L182)
