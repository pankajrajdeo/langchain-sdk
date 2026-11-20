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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/stream/_mux.py#L424)
