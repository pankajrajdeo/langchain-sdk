---
title: "is_safe_url"
description: "Non-throwing version of validate_safe_url."
source: "https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/is_safe_url"
category: "reference"
tags: [reference, langchain-core, security, ssrf_protection, is_safe_url]
---

# is_safe_url

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_security/_ssrf_protection/is_safe_url)

Non-throwing version of `validate_safe_url`.

## Signature

```python
is_safe_url(
    url: str | AnyHttpUrl,
    *,
    allow_private: bool = False,
    allow_http: bool = True,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/_security/_ssrf_protection.py#L110)
