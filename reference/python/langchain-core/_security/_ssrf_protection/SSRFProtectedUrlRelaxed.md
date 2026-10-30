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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/_security/_ssrf_protection.py#L147)
