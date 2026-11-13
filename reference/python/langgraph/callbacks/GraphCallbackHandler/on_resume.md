---
title: "on_resume"
description: "Run when graph execution resumes from a persisted checkpoint."
source: "https://reference.langchain.com/python/langgraph/callbacks/GraphCallbackHandler/on_resume"
category: "reference"
tags: [reference, langgraph, callbacks, graphcallbackhandler, on_resume]
---

# on_resume

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/callbacks/GraphCallbackHandler/on_resume)

Run when graph execution resumes from a persisted checkpoint.

## Signature

```python
on_resume(
    self,
    event: GraphResumeEvent,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `event` | `GraphResumeEvent` | Yes | Resume lifecycle event payload. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/callbacks.py#L106)
