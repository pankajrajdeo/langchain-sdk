---
title: "LangSmithRetrieverParams"
description: "LangSmith parameters for tracing."
source: "https://reference.langchain.com/python/langchain-core/retrievers/LangSmithRetrieverParams"
category: "reference"
tags: [reference, langchain-core, retrievers, langsmithretrieverparams]
---

# LangSmithRetrieverParams

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/retrievers/LangSmithRetrieverParams)

LangSmith parameters for tracing.

## Signature

```python
LangSmithRetrieverParams()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    ls_retriever_name: str,
    ls_vector_store_provider: str | None,
    ls_embedding_provider: str | None,
    ls_embedding_model: str | None,
)
```

| Name | Type |
|------|------|
| `ls_retriever_name` | `str` |
| `ls_vector_store_provider` | `str \| None` |
| `ls_embedding_provider` | `str \| None` |
| `ls_embedding_model` | `str \| None` |

## Properties

- `ls_retriever_name`
- `ls_vector_store_provider`
- `ls_embedding_provider`
- `ls_embedding_model`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/retrievers.py#L39)
