---
title: "SUFFIXES_TO_IGNORE_REGEX"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/utils/html/SUFFIXES_TO_IGNORE_REGEX"
category: "reference"
tags: [reference, langchain-core, utils, html, suffixes_to_ignore_regex]
---

# SUFFIXES_TO_IGNORE_REGEX

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/html/SUFFIXES_TO_IGNORE_REGEX)

## Signature

```python
SUFFIXES_TO_IGNORE_REGEX = '(?!' + '|'.join([re.escape(s) + '[\\#\'\\"]' for s in SUFFIXES_TO_IGNORE]) + ')'
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/utils/html.py#L33)
