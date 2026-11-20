---
title: "SSRFProtectedUrlRelaxed"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/SSRFProtectedUrlRelaxed"
category: "reference"
tags: [reference, langchain-core, security, ssrf_protection, ssrfprotectedurlrelaxed]
---

# SSRFProtectedUrlRelaxed

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/SSRFProtectedUrlRelaxed)

## Signature

```python
SSRFProtectedUrlRelaxed = Annotated[HttpUrl, BeforeValidator(_validate_url_ssrf_relaxed)]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/_security/_ssrf_protection.py#L147)
