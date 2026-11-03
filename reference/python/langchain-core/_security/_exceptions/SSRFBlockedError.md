---
title: "SSRFBlockedError"
description: "Raised when a request is blocked by SSRF protection policy."
source: "https://reference.langchain.com/python/langchain-core/_security/_exceptions/SSRFBlockedError"
category: "reference"
tags: [reference, langchain-core, security, exceptions, ssrfblockederror]
---

# SSRFBlockedError

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_exceptions/SSRFBlockedError)

Raised when a request is blocked by SSRF protection policy.

## Signature

```python
SSRFBlockedError(
    self,
    reason: str,
)
```

## Extends

- `Exception`

## Constructors

```python
__init__(
    self,
    reason: str,
) -> None
```

| Name | Type |
|------|------|
| `reason` | `str` |

## Properties

- `reason`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/_security/_exceptions.py#L4)
