---
title: "ssrf_safe_async_client"
description: "Create an httpx.AsyncClient with SSRF protection."
source: "https://reference.langchain.com/python/langchain-core/_security/_transport/ssrf_safe_async_client"
category: "reference"
tags: [reference, langchain-core, security, transport, ssrf_safe_async_client]
---

# ssrf_safe_async_client

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_transport/ssrf_safe_async_client)

Create an `httpx.AsyncClient` with SSRF protection.

Drop-in replacement for `httpx.AsyncClient(...)` - callers just swap
the constructor call.  Transport-specific kwargs (`verify`, `cert`,
`retries`, etc.) are forwarded to the inner `AsyncHTTPTransport`;
everything else goes to the `AsyncClient`.

## Signature

```python
ssrf_safe_async_client(
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
    **kwargs: object = {},
) -> httpx.AsyncClient
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/_security/_transport.py#L226)
