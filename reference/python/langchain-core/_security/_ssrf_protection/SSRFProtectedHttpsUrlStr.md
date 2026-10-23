---
title: "SSRFProtectedHttpsUrlStr"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/SSRFProtectedHttpsUrlStr"
category: "reference"
tags: [reference, langchain-core, security, ssrf_protection, ssrfprotectedhttpsurlstr]
---

# SSRFProtectedHttpsUrlStr

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/SSRFProtectedHttpsUrlStr)

## Signature

```python
SSRFProtectedHttpsUrlStr = Annotated[str, BeforeValidator(_validate_url_ssrf_https_only)]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/_security/_ssrf_protection.py#L153)
