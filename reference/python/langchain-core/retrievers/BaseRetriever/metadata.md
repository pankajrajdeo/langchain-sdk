---
title: "metadata"
description: "Optional metadata associated with the retriever."
source: "https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/metadata"
category: "reference"
tags: [reference, langchain-core, retrievers, baseretriever, metadata]
---

# metadata

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/retrievers/BaseRetriever/metadata)

Optional metadata associated with the retriever.

This metadata will be associated with each call to this retriever,
and passed as arguments to the handlers defined in `callbacks`.

You can use these to eg identify a specific instance of a retriever with its
use case.

## Signature

```python
metadata: dict[str, Any] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/retrievers.py#L135)
