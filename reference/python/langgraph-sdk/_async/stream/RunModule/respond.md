---
title: "respond"
description: "Reply to a server-side interrupt and resume the run."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule/respond"
category: "reference"
tags: [reference, langgraph-sdk, async, stream, runmodule, respond]
---

# respond

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule/respond)

Reply to a server-side interrupt and resume the run.

## Signature

```python
respond(
    self,
    response: Any,
    *,
    interrupt_id: str | None = None,
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `response` | `Any` | Yes | the response value forwarded as `params.response` on the wire (protocol field name). |
| `interrupt_id` | `str \| None` | No | optional explicit id. When omitted, requires exactly one outstanding interrupt and uses its id. (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/_async/stream.py#L214)
