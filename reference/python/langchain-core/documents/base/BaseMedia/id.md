---
title: "id"
description: "An optional identifier for the document."
source: "https://reference.langchain.com/python/langchain-core/documents/base/BaseMedia/id"
category: "reference"
tags: [reference, langchain-core, documents, base, basemedia, id]
---

# id

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/documents/base/BaseMedia/id)

An optional identifier for the document.

Ideally this should be unique across the document collection and formatted
as a UUID, but this will not be enforced.

## Signature

```python
id: str | None = Field(default=None, coerce_numbers_to_str=True)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/documents/base.py#L48)
