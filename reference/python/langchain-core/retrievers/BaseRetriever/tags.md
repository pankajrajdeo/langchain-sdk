---
title: "tags"
description: "Optional list of tags associated with the retriever."
source: "https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/tags"
category: "reference"
tags: [reference, langchain-core, retrievers, baseretriever, tags]
---

# tags

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/tags)

Optional list of tags associated with the retriever.

These tags will be associated with each call to this retriever,
and passed as arguments to the handlers defined in `callbacks`.

You can use these to eg identify a specific instance of a retriever with its
use case.

## Signature

```python
tags: list[str] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/retrievers.py#L125)
