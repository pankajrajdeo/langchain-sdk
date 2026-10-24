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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/stream/_types.py#L186)
