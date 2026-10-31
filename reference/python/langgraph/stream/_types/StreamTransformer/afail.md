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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/stream/_types.py#L216)
