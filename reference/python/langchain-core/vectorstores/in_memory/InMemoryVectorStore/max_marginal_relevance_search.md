---
title: "max_marginal_relevance_search"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/max_marginal_relevance_search"
category: "reference"
tags: [reference, langchain-core, vectorstores, in_memory, inmemoryvectorstore, max_marginal_relevance_search]
---

# max_marginal_relevance_search

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/max_marginal_relevance_search)

## Signature

```python
max_marginal_relevance_search(
    self,
    query: str,
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    kwargs: Any = {},
) -> list[Document]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/vectorstores/in_memory.py#L450)
