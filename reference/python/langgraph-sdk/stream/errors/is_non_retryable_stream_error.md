---
title: "is_non_retryable_stream_error"
description: "Whether reopening the stream would fail the same way."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/errors/is_non_retryable_stream_error"
category: "reference"
tags: [reference, langgraph-sdk, stream, errors, is_non_retryable_stream_error]
---

# is_non_retryable_stream_error

> **Function** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/errors/is_non_retryable_stream_error)

Whether reopening the stream would fail the same way.

True for a 4xx other than 408 and 429: the status of a refused stream request
or WebSocket upgrade, or a WebSocket close code of 4000 plus that status. A
server that rejects a WebSocket after accepting it closes with such a code,
because a browser can't read the status of a refused upgrade.

## Signature

```python
is_non_retryable_stream_error(
    error: BaseException | None,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/stream/errors.py#L32)
