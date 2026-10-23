---
title: "stream_error_frame"
description: "Return the error in an unsolicited {\"type\": \"error\", \"id\": null} frame."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/errors/stream_error_frame"
category: "reference"
tags: [reference, langgraph-sdk, stream, errors, stream_error_frame]
---

# stream_error_frame

> **Function** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/errors/stream_error_frame)

Return the error in an unsolicited `{"type": "error", "id": null}` frame.

The server sends one just before it closes a thread stream whose read failed.

## Signature

```python
stream_error_frame(
    event: Any,
) -> RuntimeError | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/stream/errors.py#L18)
