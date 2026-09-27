---
title: "encoding_matcher"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/encoding_matcher"
category: "reference"
tags: [reference, langchain-core, output_parsers, xml, xmloutputparser, encoding_matcher]
---

# encoding_matcher

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/xml/XMLOutputParser/encoding_matcher)

## Signature

```python
encoding_matcher: re.Pattern[str] = re.compile('<([^>]*encoding[^>]*)>\\n(.*)', re.MULTILINE | re.DOTALL)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/output_parsers/xml.py#L174)
