---
title: "abort"
description: "Stop the run early."
source: "https://reference.langchain.com/python/langgraph/stream/run_stream/AsyncGraphRunStream/abort"
category: "reference"
tags: [reference, langgraph, stream, run_stream, asyncgraphrunstream, abort]
---

# abort

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/run_stream/AsyncGraphRunStream/abort)

Stop the run early.

Marks the stream exhausted and wakes any pump-waiters. Cancels an
in-flight pull if one is running, then closes the underlying graph
iterator, so running nodes and nested subgraphs are cancelled
whether or not a pump is mid-pull. Closes the mux; any `apush`
blocked on backpressure wakes and returns without appending.
Idempotent.

## Signature

```python
abort(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/stream/run_stream.py#L530)
