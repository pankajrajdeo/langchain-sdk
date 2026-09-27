---
title: "max_marginal_relevance_search_by_vector"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/max_marginal_relevance_search_by_vector"
category: "reference"
tags: [reference, langchain-core, vectorstores, in_memory, inmemoryvectorstore, max_marginal_relevance_search_by_vector]
---

# max_marginal_relevance_search_by_vector

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/in_memory/InMemoryVectorStore/max_marginal_relevance_search_by_vector)

## Signature

```python
max_marginal_relevance_search_by_vector(
    self,
    embedding: list[float],
    k: int = 4,
    fetch_k: int = 20,
    lambda_mult: float = 0.5,
    *,
    filter: Callable[[Document], bool] | None = None,
    **kwargs: Any = {},
) -> list[Document]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/vectorstores/in_memory.py#L418)
