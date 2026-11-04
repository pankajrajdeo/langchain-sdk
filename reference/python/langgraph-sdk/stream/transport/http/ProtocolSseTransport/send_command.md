---
title: "send_command"
description: "POST a command. Returns the response JSON, or None for 202/204."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/transport/http/ProtocolSseTransport/send_command"
category: "reference"
tags: [reference, langgraph-sdk, stream, transport, http, protocolssetransport, send_command]
---

# send_command

> **Method** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/transport/http/ProtocolSseTransport/send_command)

POST a command. Returns the response JSON, or `None` for 202/204.

## Signature

```python
send_command(
    self,
    command: dict[str, Any],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/stream/transport/http.py#L64)
