---
title: "afail"
description: "Fail on the async lane."
source: "https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/afail"
category: "reference"
tags: [reference, langgraph, stream, mux, streammux, afail]
---

# afail

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_mux/StreamMux/afail)

Fail on the async lane.

Cancels every scheduled task across all transformers, awaits
them to completion, then runs each transformer's `afail` hook
and auto-fails channels and the main event log.

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/stream/_mux.py#L424)
