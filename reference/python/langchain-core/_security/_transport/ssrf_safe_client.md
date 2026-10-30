---
title: "ssrf_safe_client"
description: "Create an httpx.Client with SSRF protection."
source: "https://reference.langchain.com/python/langchain-core/_security/_transport/ssrf_safe_client"
category: "reference"
tags: [reference, langchain-core, security, transport, ssrf_safe_client]
---

# ssrf_safe_client

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_transport/ssrf_safe_client)

Create an `httpx.Client` with SSRF protection.

## Signature

```python
ssrf_safe_client(
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
    kwargs: object = {},
) -> httpx.Client
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/_security/_transport.py#L202)
