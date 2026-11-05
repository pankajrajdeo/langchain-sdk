---
title: "start"
description: "Send run.start to the server. Returns the result ({\"run_id\": ...})."
source: "https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncRunModule/start"
category: "reference"
tags: [reference, langgraph-sdk, sync, stream, syncrunmodule, start]
---

# start

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_sync/stream/SyncRunModule/start)

Send `run.start` to the server. Returns the result (`{"run_id": ...}`).

## Signature

```python
start(
    self,
    *,
    input: Any = None,
    config: dict[str, Any] | None = None,
    metadata: dict[str, Any] | None = None,
    langsmith_tracing: LangSmithTracing | None = None,
) -> dict[str, Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/_sync/stream.py#L222)
