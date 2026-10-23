---
title: "SSRFSafeSyncTransport"
description: "httpx sync transport that validates DNS results against an SSRF policy."
source: "https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeSyncTransport"
category: "reference"
tags: [reference, langchain-core, security, transport, ssrfsafesynctransport]
---

# SSRFSafeSyncTransport

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeSyncTransport)

httpx sync transport that validates DNS results against an SSRF policy.

Sync mirror of `SSRFSafeTransport`. See that class for full documentation.

## Signature

```python
SSRFSafeSyncTransport(
    self,
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
    transport_kwargs: object = {},
)
```

## Extends

- `httpx.BaseTransport`

## Constructors

```python
__init__(
    self,
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
    transport_kwargs: object = {},
) -> None
```

| Name | Type |
|------|------|
| `policy` | `SSRFPolicy` |
| `transport_kwargs` | `object` |

## Methods

- [`handle_request()`](https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeSyncTransport/handle_request)
- [`close()`](https://reference.langchain.com/python/langchain-core/_security/_transport/SSRFSafeSyncTransport/close)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/_security/_transport.py#L130)
