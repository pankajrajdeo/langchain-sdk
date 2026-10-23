---
title: "PREFIXES_TO_IGNORE_REGEX"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/utils/html/PREFIXES_TO_IGNORE_REGEX"
category: "reference"
tags: [reference, langchain-core, utils, html, prefixes_to_ignore_regex]
---

# PREFIXES_TO_IGNORE_REGEX

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/html/PREFIXES_TO_IGNORE_REGEX)

## Signature

```python
PREFIXES_TO_IGNORE_REGEX = '(?!' + '|'.join([re.escape(s) for s in PREFIXES_TO_IGNORE]) + ')'
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/utils/html.py#L37)
