# VoyageAI integrations

> Integrate with VoyageAI using LangChain Python.

All functionality related to VoyageAI

> [VoyageAI](https://www.voyageai.com/) Voyage AI builds embedding models, customized for your domain and company, for better retrieval quality.

## Installation and setup

Install the integration package with

```bash
pip install langchain-voyageai
```

```bash
uv add langchain-voyageai
```

Get a VoyageAI API key and set it as an environment variable (`VOYAGE_API_KEY`)

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

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/voyageai.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
