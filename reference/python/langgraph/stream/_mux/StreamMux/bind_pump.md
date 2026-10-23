---
title: "bind_pump"
description: "Wire the sync pull callback onto every projection in this mux."
source: "https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/bind_pump"
category: "reference"
tags: [reference, langgraph, stream, mux, streammux, bind_pump]
---

# bind_pump

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/bind_pump)

Wire the sync pull callback onto every projection in this mux.

Records the pump on the mux so child mini-muxes built by
`_make_child` can inherit it. Propagates to:
- the main event log (`self._events`)
- every projection StreamChannel in `extensions`
- any registered transformer that exposes `_bind_pump` (e.g.
  `MessagesTransformer` so `ChatModelStream` instances drive the
  shared pump from their cursors)

## Signature

```python
bind_pump(
    self,
    fn: Callable[[], bool],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/stream/_mux.py#L162)
