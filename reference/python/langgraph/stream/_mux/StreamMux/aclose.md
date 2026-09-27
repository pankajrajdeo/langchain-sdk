---
title: "aclose"
description: "Finalize on the async lane."
source: "https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/aclose"
category: "reference"
tags: [reference, langgraph, stream, mux, streammux, aclose]
---

# aclose

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/aclose)

Finalize on the async lane.

Awaits every task started via `StreamTransformer.schedule()`
across all transformers, then calls `afinalize()` on each,
then auto-closes channels and the main event log.

If any scheduled task raised under `on_error="raise"`, or any
transformer's `afinalize` raises, the exception propagates.
The caller (the pump) handles it by routing into `afail`.

## Signature

```python
aclose(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/stream/_mux.py#L380)
