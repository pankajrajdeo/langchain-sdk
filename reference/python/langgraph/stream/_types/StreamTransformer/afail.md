---
title: "afail"
description: "Called when the run ends with an error (async lane)."
source: "https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/afail"
category: "reference"
tags: [reference, langgraph, stream, types, streamtransformer, afail]
---

# afail

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/StreamTransformer/afail)

Called when the run ends with an error (async lane).

The mux cancels and awaits every task started via `schedule()`
before calling this, so cleanup doesn't race with in-flight work.

The default delegates to `fail`.

## Signature

```python
afail(
    self,
    err: BaseException,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `err` | `BaseException` | Yes | The exception that ended the run. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/stream/_types.py#L216)
