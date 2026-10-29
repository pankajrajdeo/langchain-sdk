---
title: "SSRFProtectedHttpsUrl"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/SSRFProtectedHttpsUrl"
category: "reference"
tags: [reference, langchain-core, security, ssrf_protection, ssrfprotectedhttpsurl]
---

# SSRFProtectedHttpsUrl

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/SSRFProtectedHttpsUrl)

## Signature

```python
SSRFProtectedHttpsUrl = Annotated[HttpUrl, BeforeValidator(_validate_url_ssrf_https_only)]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/_security/_ssrf_protection.py#L150)
