---
title: "validate_url"
description: "Validate a URL against the SSRF policy, including DNS resolution."
source: "https://reference.langchain.com/python/langchain-core/_security/_policy/validate_url"
category: "reference"
tags: [reference, langchain-core, security, policy, validate_url]
---

# validate_url

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_policy/validate_url)

Validate a URL against the SSRF policy, including DNS resolution.

This is the primary entry-point for async code paths. It delegates
scheme/hostname/allowed-hosts checks to `validate_url_sync`, then
resolves DNS and validates every resolved IP.

## Signature

```python
validate_url(
    url: str,
    policy: SSRFPolicy = DEFAULT_SSRF_POLICY,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/_security/_policy.py#L250)
