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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/2b7ff14fb2021e6f4ee22f796a9b888eaacb5af9/libs/core/langchain_core/_security/_ssrf_protection.py#L153)
