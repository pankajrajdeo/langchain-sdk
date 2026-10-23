---
title: "from_texts"
description: "Return VectorStore initialized from texts and embeddings."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/from_texts"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, from_texts]
---

# from_texts

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/from_texts)

Return `VectorStore` initialized from texts and embeddings.

## Signature

```python
from_texts(
    cls: type[VST],
    texts: list[str],
    embedding: Embeddings,
    metadatas: list[dict[str, Any]] | None = None,
    *,
    ids: list[str] | None = None,
    kwargs: Any = {},
) -> VST
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `texts` | `list[str]` | Yes | Texts to add to the `VectorStore`. |
| `embedding` | `Embeddings` | Yes | Embedding function to use. |
| `metadatas` | `list[dict[str, Any]] \| None` | No | Optional list of metadatas associated with the texts. (default: `None`) |
| `ids` | `list[str] \| None` | No | Optional list of IDs associated with the texts. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`VST`

`VectorStore` initialized from texts and embeddings.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/vectorstores/base.py#L846)
