---
title: "tap_output_aiter"
description: "Pass-through — required by the _StreamingCallbackHandler protocol."
source: "https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/tap_output_aiter"
category: "reference"
tags: [reference, langgraph, pregel, tools, streamtoolcallhandler, tap_output_aiter]
---

# tap_output_aiter

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/tap_output_aiter)

Pass-through — required by the `_StreamingCallbackHandler` protocol.

## Signature

```python
tap_output_aiter(
    self,
    run_id: UUID,
    output: AsyncIterator[T],
) -> AsyncIterator[T]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/pregel/_tools.py#L203)
