---
title: "finalize"
description: "Called when the run ends normally (sync lane)."
source: "https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/finalize"
category: "reference"
tags: [reference, langgraph, stream, types, streamtransformer, finalize]
---

# finalize

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/finalize)

Called when the run ends normally (sync lane).

Override to close StreamChannels, resolve promises, or perform
other teardown. StreamChannel instances in the projection dict
are auto-closed by the mux.

## Signature

```python
finalize(
    self,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/stream/_types.py#L186)
