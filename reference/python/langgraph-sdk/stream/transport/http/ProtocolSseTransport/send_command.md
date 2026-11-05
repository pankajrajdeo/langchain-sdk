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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/stream/transport/http.py#L64)
