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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/_security/_ssrf_protection.py#L150)
