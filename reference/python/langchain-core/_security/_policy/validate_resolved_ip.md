---
title: "validate_resolved_ip"
description: "Validate a resolved IP address against the SSRF policy."
source: "https://reference.langchain.com/python/langchain-core/_security/_policy/validate_resolved_ip"
category: "reference"
tags: [reference, langchain-core, security, policy, validate_resolved_ip]
---

# validate_resolved_ip

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_policy/validate_resolved_ip)

Validate a resolved IP address against the SSRF policy.

Raises SSRFBlockedError if the IP is blocked.

## Signature

```python
validate_resolved_ip(
    ip_str: str,
    policy: SSRFPolicy,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/_security/_policy.py#L198)
