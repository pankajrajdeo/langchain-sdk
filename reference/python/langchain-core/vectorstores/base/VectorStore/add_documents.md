---
title: "add_documents"
description: "Add or update documents in the VectorStore."
source: "https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/add_documents"
category: "reference"
tags: [reference, langchain-core, vectorstores, base, vectorstore, add_documents]
---

# add_documents

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/vectorstores/base/VectorStore/add_documents)

Add or update documents in the `VectorStore`.

## Signature

```python
add_documents(
    self,
    documents: list[Document],
    **kwargs: Any = {},
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `list[Document]` | Yes | Documents to add to the `VectorStore`. |
| `**kwargs` | `Any` | No | Additional keyword arguments.  If kwargs contains IDs and documents contain ids, the IDs in the kwargs will receive precedence. (default: `{}`) |

## Returns

`list[str]`

List of IDs of the added texts.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/vectorstores/base.py#L234)
