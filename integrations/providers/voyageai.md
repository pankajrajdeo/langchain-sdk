---
title: "VoyageAI by MongoDB integrations"
description: "Integrate with VoyageAI by MongoDB using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/providers/voyageai"
category: "docs"
tags: [docs, integrations, providers, voyageai]
---

# VoyageAI by MongoDB integrations

> Integrate with VoyageAI by MongoDB using LangChain Python.

All functionality related to VoyageAI by MongoDB

> [VoyageAI by MongoDB](https://www.voyageai.com/) builds embedding models, customized for your domain and company, for better retrieval quality.

## Installation and setup

Install the integration package with

**pip**

```bash
pip install langchain-voyageai
```

**uv**

```bash
uv add langchain-voyageai
```

Get a VoyageAI by MongoDB API key and set it as an environment variable (`VOYAGE_API_KEY`)

## Text embedding model

See a [usage example](../embeddings/voyageai.md).

```python
from langchain_voyageai import VoyageAIEmbeddings
```

## Reranking

See a [usage example](../document_transformers/voyageai-reranker.md).

```python
from langchain_voyageai import VoyageAIRerank
```

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/voyageai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
