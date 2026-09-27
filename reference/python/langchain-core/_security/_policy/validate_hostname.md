---
title: "validate_hostname"
description: "Validate a hostname against the SSRF policy."
source: "https://reference.langchain.com/python/langchain-core/_security/_policy/validate_hostname"
category: "reference"
tags: [reference, langchain-core, security, policy, validate_hostname]
---

# validate_hostname

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_policy/validate_hostname)

Validate a hostname against the SSRF policy.

Raises SSRFBlockedError if the hostname is blocked.

## Signature

```python
validate_hostname(
    hostname: str,
    policy: SSRFPolicy,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/_security/_policy.py#L215)
