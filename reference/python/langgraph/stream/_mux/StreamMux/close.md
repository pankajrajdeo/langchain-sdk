---
title: "close"
description: "Finalize all transformers, close all projections and the main log."
source: "https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/close"
category: "reference"
tags: [reference, langgraph, stream, mux, streammux, close]
---

# close

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/close)

Finalize all transformers, close all projections and the main log.

StreamChannels discovered in transformer projections are
auto-closed after `finalize()` runs — transformers don't need
to close them manually. If any transformer's `finalize()` raises,
the remaining transformers, projections, and the main log are
still closed; the first error is re-raised after cleanup
completes.

## Signature

```python
close(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/stream/_mux.py#L298)
