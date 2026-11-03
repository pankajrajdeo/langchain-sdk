---
title: "Graph RAG integration"
description: "Integrate with the Graph RAG retriever using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/retrievers/graph_rag"
category: "docs"
tags: [docs, integrations, retrievers, graph_rag]
---

# Graph RAG integration

> Integrate with the Graph RAG retriever using LangChain Python.

This guide provides an introduction to Graph RAG. For detailed documentation of all
supported features and configurations, refer to the
[Graph RAG Project Page](https://datastax.github.io/graph-rag/).

## Overview

The `GraphRetriever` from the `langchain-graph-retriever` package provides a LangChain
[retriever](../../deepagents/retrieval.md) that combines **unstructured** similarity search
on vectors with **structured** traversal of metadata properties. This enables graph-based
retrieval over an **existing** vector store.

### Integration details

| Retriever | Source | PyPI Package | Latest | Project Page |
| :- | :- | :-: | :-: | :-: |
| `GraphRetriever` | [github.com/datastax/graph-rag](https://github.com/datastax/graph-rag/tree/main/packages/langchain-graph-retriever) | [`langchain-graph-retriever`](https://pypi.org/project/langchain-graph-retriever/) | ![PyPI - Version](https://img.shields.io/pypi/v/langchain-graph-retriever?style=flat-square\&label=%20\&color=orange) | [Graph RAG](https://datastax.github.io/graph-rag/) |

## Benefits

* [**Link based on existing metadata:**](https://datastax.github.io/graph-rag/guide/get-started/)
  Use existing metadata fields without additional processing. Retrieve more from an
  existing vector store!

* [**Change links on demand:**](https://datastax.github.io/graph-rag/guide/edges/)
  Edges can be specified on-the-fly, allowing different relationships to be traversed
  based on the question.

* [**Pluggable Traversal Strategies:**](https://datastax.github.io/graph-rag/guide/strategies/)
  Use built-in traversal strategies like Eager or MMR, or define custom logic to select
  which nodes to explore.

* [**Broad compatibility:**](https://datastax.github.io/graph-rag/guide/adapters/)
  Adapters are available for a variety of vector stores with support for additional
  stores easily added.

## Setup

### Installation

This retriever lives in the `langchain-graph-retriever` package.

**pip**

```bash
pip install -qU langchain-graph-retriever
```

**uv**

```bash
uv add langchain-graph-retriever
```

## Instantiation

The following examples will show how to perform graph traversal over some sample
Documents about animals.

### Prerequisites

1. Ensure you have Python 3.10 or later installed.

2. Install the following package that provides sample data:

```bash
   pip install -qU graph_rag_example_helpers
```

3. Download the test documents:

```python
   from graph_rag_example_helpers.datasets.animals import fetch_documents
   animals = fetch_documents()
```

4. Select an embedding model. The vector store examples below use the resulting `embeddings` object:

> [tab] OpenAI
>
```shell
> pip install -U "langchain-openai"
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("OPENAI_API_KEY"):
>     os.environ["OPENAI_API_KEY"] = getpass.getpass("Enter API key for OpenAI: ")
>
> from langchain_openai import OpenAIEmbeddings
>
> embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

> [tab] Azure
>
```shell
> pip install -U "langchain-openai"
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("AZURE_OPENAI_API_KEY"):
>     os.environ["AZURE_OPENAI_API_KEY"] = getpass.getpass("Enter API key for Azure: ")
>
> from langchain_openai import AzureOpenAIEmbeddings
>
> embeddings = AzureOpenAIEmbeddings(
>     azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
>     azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
>     openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
> )
```

> [tab] Google Gemini
>
```shell
> pip install -qU langchain-google-genai
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("GOOGLE_API_KEY"):
>     os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")
>
> from langchain_google_genai import GoogleGenerativeAIEmbeddings
>
> embeddings = GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")
```

> [tab] Gemini Enterprise Agent Platform
>
```shell
> pip install -qU langchain-google-vertexai
```
>
```python
> from langchain_google_vertexai import VertexAIEmbeddings
>
> embeddings = VertexAIEmbeddings(model="text-embedding-005")
```

> [tab] AWS
>
```shell
> pip install -qU langchain-aws
```
>
```python
> from langchain_aws import BedrockEmbeddings
>
> embeddings = BedrockEmbeddings(model_id="amazon.titan-embed-text-v2:0")
```

> [tab] HuggingFace
>
```shell
> pip install -qU langchain-huggingface
```
>
```python
> from langchain_huggingface import HuggingFaceEmbeddings
>
> embeddings = HuggingFaceEmbeddings(
>     model_name="sentence-transformers/all-mpnet-base-v2",
>     encode_kwargs={"normalize_embeddings": True},
> )
```

> [tab] Ollama
>
```shell
> pip install -qU langchain-ollama
```
>
```python
> from langchain_ollama import OllamaEmbeddings
>
> embeddings = OllamaEmbeddings(model="llama3")
```

> [tab] Cohere
>
```shell
> pip install -qU langchain-cohere
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("COHERE_API_KEY"):
>     os.environ["COHERE_API_KEY"] = getpass.getpass("Enter API key for Cohere: ")
>
> from langchain_cohere import CohereEmbeddings
>
> embeddings = CohereEmbeddings(model="embed-english-v3.0")
```

> [tab] MistralAI
>
```shell
> pip install -qU langchain-mistralai
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("MISTRALAI_API_KEY"):
>     os.environ["MISTRALAI_API_KEY"] = getpass.getpass("Enter API key for MistralAI: ")
>
> from langchain_mistralai import MistralAIEmbeddings
>
> embeddings = MistralAIEmbeddings(model="mistral-embed")
```

> [tab] Nomic
>
```shell
> pip install -qU langchain-nomic
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("NOMIC_API_KEY"):
>     os.environ["NOMIC_API_KEY"] = getpass.getpass("Enter API key for Nomic: ")
>
> from langchain_nomic import NomicEmbeddings
>
> embeddings = NomicEmbeddings(model="nomic-embed-text-v1.5")
```

> [tab] NVIDIA
>
```shell
> pip install -qU langchain-nvidia-ai-endpoints
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("NVIDIA_API_KEY"):
>     os.environ["NVIDIA_API_KEY"] = getpass.getpass("Enter API key for NVIDIA: ")
>
> from langchain_nvidia_ai_endpoints import NVIDIAEmbeddings
>
> embeddings = NVIDIAEmbeddings(model="NV-Embed-QA")
```

> [tab] Voyage AI
>
```shell
> pip install -qU langchain-voyageai
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("VOYAGE_API_KEY"):
>     os.environ["VOYAGE_API_KEY"] = getpass.getpass("Enter API key for Voyage AI: ")
>
> from langchain_voyageai import VoyageAIEmbeddings
>
> embeddings = VoyageAIEmbeddings(model="voyage-3")
```

> [tab] IBM watsonx
>
```shell
> pip install -qU langchain-ibm
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("WATSONX_APIKEY"):
>     os.environ["WATSONX_APIKEY"] = getpass.getpass("Enter API key for IBM watsonx: ")
>
> from langchain_ibm import WatsonxEmbeddings
>
> embeddings = WatsonxEmbeddings(
>     model_id="ibm/slate-125m-english-rtrvr",
>     url="https://us-south.ml.cloud.ibm.com",
>     project_id="<WATSONX PROJECT_ID>",
> )
```

> [tab] Fake
>
```shell
> pip install -qU langchain-core
```
>
```python
> from langchain_core.embeddings import DeterministicFakeEmbedding
>
> embeddings = DeterministicFakeEmbedding(size=4096)
```

> [tab] Isaacus
>
```shell
> pip install -qU langchain-isaacus
```
>
```python
> import getpass
> import os
>
> if not os.environ.get("ISAACUS_API_KEY"):
>     os.environ["ISAACUS_API_KEY"] = getpass.getpass("Enter API key for Isaacus: ")
>
> from langchain_isaacus import IsaacusEmbeddings
>
> embeddings = IsaacusEmbeddings(model="kanon-2-embedder")
```

### Populating the vector store

This section shows how to populate a variety of vector stores with the sample data.

For help on choosing one of the vector stores below, or to add support for your
vector store, consult the documentation about
[Adapters and Supported Stores](https://datastax.github.io/graph-rag/guide/adapters/).

> [tab] AstraDB
>
> Install the `langchain-graph-retriever` package with the `astra` extra:
>
```bash
> pip install "langchain-graph-retriever[astra]"
```
>
> Then create a vector store and load the test documents:
>
```python
> from langchain_astradb import AstraDBVectorStore
>
> vector_store = AstraDBVectorStore.from_documents(
>     documents=animals,
>     embedding=embeddings,
>     collection_name="animals",
>     api_endpoint=ASTRA_DB_API_ENDPOINT,
>     token=ASTRA_DB_APPLICATION_TOKEN,
> )
```
>
> For the `ASTRA_DB_API_ENDPOINT` and `ASTRA_DB_APPLICATION_TOKEN` credentials,
> consult the [AstraDB Vector Store Guide](../vectorstores/astradb.md).
>
> > [!NOTE]
> >
> > For faster initial testing, consider using the **InMemory** Vector Store.

> [tab] Chroma
>
> Install the `langchain-graph-retriever` package with the `chroma` extra:
>
```bash
> pip install "langchain-graph-retriever[chroma]"
```
>
> Then create a vector store and load the test documents:
>
```python
> from langchain_chroma.vectorstores import Chroma
> from langchain_graph_retriever.transformers import ShreddingTransformer
>
> vector_store = Chroma.from_documents(
>     documents=list(ShreddingTransformer().transform_documents(animals)),
>     embedding=embeddings,
>     collection_name="animals",
> )
```
>
> For help creating a Chroma connection, consult the [Chroma Vector Store Guide](../vectorstores/chroma.md).
>
> > [!NOTE]
> >
> > Chroma doesn't support searching in nested metadata. Because of this
> > it is necessary to use the [`ShreddingTransformer`](https://datastax.github.io/graph-rag/reference/langchain_graph_retriever/transformers/#langchain_graph_retriever.transformers.shredding.ShreddingTransformer)
> > when inserting documents.

> [tab] InMemory
>
> Install the `langchain-graph-retriever` package:
>
```bash
> pip install "langchain-graph-retriever"
```
>
> Then create a vector store and load the test documents:
>
```python
> from langchain_core.vectorstores import InMemoryVectorStore
>
> vector_store = InMemoryVectorStore.from_documents(
>     documents=animals,
>     embedding=embeddings,
> )
```
>
> > [!TIP]
> >
> > Using the `InMemoryVectorStore` is the fastest way to get started with Graph RAG
> > but it isn't recommended for production use. Instead it is recommended to use
> > **AstraDB** or **OpenSearch**.

### Graph traversal

This graph retriever starts with a single animal that best matches the query, then
traverses to other animals sharing the same `habitat` and/or `origin`.

```python
from graph_retriever.strategies import Eager
from langchain_graph_retriever import GraphRetriever

traversal_retriever = GraphRetriever(
    store = vector_store,
    edges = [("habitat", "habitat"), ("origin", "origin")],
    strategy = Eager(k=5, start_k=1, max_depth=2),
)
```

The above creates a graph traversing retriever that starts with the nearest
animal (`start_k=1`), retrieves 5 documents (`k=5`) and limits the search to documents
that are at most 2 steps away from the first animal (`max_depth=2`).

The `edges` define how metadata values can be used for traversal. In this case, every
animal is connected to other animals with the same `habitat` and/or `origin`.

```python
results = traversal_retriever.invoke("what animals could be found near a capybara?")

for doc in results:
    print(f"{doc.id}: {doc.page_content}")
```

```text
capybara: capybaras are the largest rodents in the world and are highly social animals.
heron: herons are wading birds known for their long legs and necks, often seen near water.
crocodile: crocodiles are large reptiles with powerful jaws and a long lifespan, often living over 70 years.
frog: frogs are amphibians known for their jumping ability and croaking sounds.
duck: ducks are waterfowl birds known for their webbed feet and quacking sounds.
```

Graph traversal improves retrieval quality by leveraging structured relationships in
the data. Unlike standard similarity search (see below), it provides a clear,
explainable rationale for why documents are selected.

In this case, the documents `capybara`, `heron`, `frog`, `crocodile`, and `newt` all
share the same `habitat=wetlands`, as defined by their metadata. This should increase
Document Relevance and the quality of the answer from the LLM.

### Comparison to standard retrieval

When `max_depth=0`, the graph traversing retriever behaves like a standard retriever:

```python
standard_retriever = GraphRetriever(
    store = vector_store,
    edges = [("habitat", "habitat"), ("origin", "origin")],
    strategy = Eager(k=5, start_k=5, max_depth=0),
)
```

This creates a retriever that starts with the nearest 5 animals (`start_k=5`),
and returns them without any traversal (`max_depth=0`). The edge definitions
are ignored in this case.

This is essentially the same as:

```python
standard_retriever = vector_store.as_retriever(search_kwargs={"k":5})
```

For either case, invoking the retriever returns:

```python
results = standard_retriever.invoke("what animals could be found near a capybara?")

for doc in results:
    print(f"{doc.id}: {doc.page_content}")
```

```text
capybara: capybaras are the largest rodents in the world and are highly social animals.
iguana: iguanas are large herbivorous lizards often found basking in trees and near water.
guinea pig: guinea pigs are small rodents often kept as pets due to their gentle and social nature.
hippopotamus: hippopotamuses are large semi-aquatic mammals known for their massive size and territorial behavior.
boar: boars are wild relatives of pigs, known for their tough hides and tusks.
```

These documents are joined based on similarity alone. Any structural data that existed
in the store is ignored. As compared to graph retrieval, this can decrease Document
Relevance because the returned results have a lower chance of being helpful to answer
the query.

## Usage

Following the examples above, `invoke` is used to initiate retrieval on a query.

## API reference

To explore all available parameters and advanced configurations, refer to the
[Graph RAG API reference](https://datastax.github.io/graph-rag/reference/).

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/retrievers/graph_rag.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
