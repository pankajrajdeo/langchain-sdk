---
title: "validate_url_sync"
description: "Synchronous URL validation (no DNS resolution)."
source: "https://reference.langchain.com/python/langchain-core/_security/_policy/validate_url_sync"
category: "reference"
tags: [reference, langchain-core, security, policy, validate_url_sync]
---

# validate_url_sync

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_policy/validate_url_sync)

Synchronous URL validation (no DNS resolution).

Suitable for Pydantic validators and other sync contexts. Checks scheme
and hostname patterns only - use `validate_url` for full DNS-aware checking.

## Signature

```python
validate_url_sync(
    url: str,
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/_security/_policy.py#L278)
