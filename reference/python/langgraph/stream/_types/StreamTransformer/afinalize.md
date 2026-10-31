---
title: "afinalize"
description: "Called when the run ends normally (async lane)."
source: "https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/afinalize"
category: "reference"
tags: [reference, langgraph, stream, types, streamtransformer, afinalize]
---

# afinalize

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/afinalize)

Called when the run ends normally (async lane).

By the time this runs, the mux has already awaited every task
started via `schedule()`, so StreamChannels can be closed here
without a last-task-wins race.

The default delegates to `finalize`.

## Signature

```python
afinalize(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/stream/_types.py#L194)
