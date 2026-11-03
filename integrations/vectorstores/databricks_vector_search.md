---
title: "Databricks vector search integration"
description: "Integrate with the Databricks vector search vector store using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/vectorstores/databricks_vector_search"
category: "docs"
tags: [docs, integrations, vectorstores, databricks_vector_search]
---

# Databricks vector search integration

> Integrate with the Databricks vector search vector store using LangChain Python.

[Databricks Vector Search](https://docs.databricks.com/en/generative-ai/vector-search.html) is a serverless similarity search engine that allows you to store a vector representation of your data, including metadata, in a vector database. With Vector Search, you can create auto-updating vector search indexes from Delta tables managed by Unity Catalog and query them with a simple API to return the most similar vectors.

This notebook shows how to use LangChain with Databricks Vector Search.

## Setup

To access Databricks models you'll need to create a Databricks account, set up credentials (only if you are outside Databricks workspace), and install required packages.

### Credentials (only if you are outside databricks)

If you are running LangChain app inside Databricks, you can skip this step.

Otherwise, you need manually set the Databricks workspace hostname and personal access token to `DATABRICKS_HOST` and `DATABRICKS_TOKEN` environment variables, respectively. See [Authentication Documentation](https://docs.databricks.com/en/dev-tools/auth/index.html#databricks-personal-access-tokens) for how to get an access token.

```python
import getpass
import os

os.environ["DATABRICKS_HOST"] = "https://your-databricks-workspace"
if "DATABRICKS_TOKEN" not in os.environ:
    os.environ["DATABRICKS_TOKEN"] = getpass.getpass(
        "Enter your Databricks access token: "
    )
```

### Installation

The LangChain Databricks integration lives in the `databricks-langchain` package.

```python
pip install -qU databricks-langchain
```

### Create a vector search endpoint and index (if you haven't already)

In this section, we will create a Databricks Vector Search endpoint and an index using the client SDK.

If you already have an endpoint and an index, you can skip the section and go straight to "Instantiation" section.

First, instantiate the Databricks VectorSearch client:

```python
from databricks.vector_search.client import VectorSearchClient

client = VectorSearchClient()
```

Next, we will create a new VectorSearch endpoint.

```python
endpoint_name = "<your-endpoint-name>"

client.create_endpoint(name=endpoint_name, endpoint_type="STANDARD")
```

Lastly, we will create an index that can be queried on the endpoint. There are two types of indexes in Databricks Vector Search and the `DatabricksVectorSearch` class support both use cases.

* **Delta Sync Index** automatically syncs with a source Delta Table, automatically and incrementally updating the index as the underlying data in the Delta Table changes.

* **Direct Vector Access Index** supports direct read and write of vectors and metadata. The user is responsible for updating this table using the REST API or the Python SDK.

Also for delta-sync index, you can choose to use Databricks-managed embeddings or self-managed embeddings (via LangChain embeddings classes).

The following code creates a **direct-access** index. Please refer to the [Databricks documentation](https://docs.databricks.com/en/generative-ai/create-query-vector-search.html) for the instruction to create the other type of indexes.

```python
index_name = "<your-index-name>"  # Format: "<catalog>.<schema>.<index-name>"

index = client.create_direct_access_index(
    endpoint_name=endpoint_name,
    index_name=index_name,
    primary_key="id",
    # Dimension of the embeddings. Please change according to the embedding model you are using.
    embedding_dimension=3072,
    # A column to store the embedding vectors for the text data
    embedding_vector_column="text_vector",
    schema={
        "id": "string",
        "text": "string",
        "text_vector": "array<float>",
        # Optional metadata columns
        "source": "string",
    },
)

index.describe()
```

## Instantiation

The instantiation of `DatabricksVectorSearch` is a bit different depending on whether your index uses Databricks-managed embeddings or self-managed embeddings i.e. LangChain Embeddings object of your choice.

If you are using a delta-sync index with Databricks-managed embeddings:

```python
from databricks_langchain import DatabricksVectorSearch

vector_store = DatabricksVectorSearch(
    endpoint=endpoint_name,
    index_name=index_name,
)
```

If you are using a direct-access index or a delta-sync index with self-managed embeddings,
you also need to provide the embedding model and text column in your source table to
use for the embeddings:

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

```python
# | output: false
# | echo: false
from langchain_openai import OpenAIEmbeddings

embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
```

```python
vector_store = DatabricksVectorSearch(
    endpoint=endpoint_name,
    index_name=index_name,
    embedding=embeddings,
    # The column name in the index that contains the text data to be embedded
    text_column="document_content",
)
```

## Manage vector store

### Add items to vector store

Note: Adding items to vector store via `add_documents` method is only supported for a **direct-access** index.

```python
from langchain_core.documents import Document

document_1 = Document(page_content="foo", metadata={"source": "https://example.com"})

document_2 = Document(page_content="bar", metadata={"source": "https://example.com"})

document_3 = Document(page_content="baz", metadata={"source": "https://example.com"})

documents = [document_1, document_2, document_3]

vector_store.add_documents(documents=documents, ids=["1", "2", "3"])
```

```python
['1', '2', '3']
```

### Delete items from vector store

Note: Deleting items to vector store via `delete` method is only supported for a **direct-access** index.

```python
vector_store.delete(ids=["3"])
```

```text
True
```

## Query vector store

Once your vector store has been created and the relevant documents have been added you will most likely wish to query it during the running of your chain or agent.

### Query directly

Performing a simple similarity search can be done as follows:

```python
results = vector_store.similarity_search(
    query="thud", k=1, filter={"source": "https://example.com"}
)
for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")
```

```text
* foo [{'id': '1'}]
```

Note: By default, similarity search only returns the primary key and text column. If you want to retrieve the custom metadata associated with the document, pass the additional columns in the `columns` parameter when initializing the vector store.

```python
vector_store = DatabricksVectorSearch(
    endpoint=endpoint_name,
    index_name=index_name,
    embedding=embeddings,
    text_column="text",
    columns=["source"],
)

results = vector_store.similarity_search(query="thud", k=1)
for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")
```

```text
* foo [{'source': 'https://example.com', 'id': '1'}]
```

If you want to execute a similarity search and receive the corresponding scores you can run:

```python
results = vector_store.similarity_search_with_score(
    query="thud", k=1, filter={"source": "https://example.com"}
)
for doc, score in results:
    print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")
```

```text
* [SIM=0.414035] foo [{'source': 'https://example.com', 'id': '1'}]
```

### Query by turning into retriever

You can also transform the vector store into a retriever for easier usage in your chains.

```python
retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 1})
retriever.invoke("thud")
```

```text
[Document(metadata={'source': 'https://example.com', 'id': '1'}, page_content='foo')]
```

## Usage for retrieval-augmented generation

For guides on how to use this vector store for retrieval-augmented generation (RAG), see the following sections:

* [Retrieval docs](../../deepagents/retrieval.md)
* [Build a RAG app with LangChain](../../deepagents/rag.md)
* [Agentic RAG](../../langgraph/agentic-rag.md)

***

## API reference

For detailed documentation of all DatabricksVectorSearch features and configurations head to the [API reference](https://api-docs.databricks.com/python/databricks-ai-bridge/latest/databricks_langchain.html#databricks_langchain.DatabricksVectorSearch).

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/vectorstores/databricks_vector_search.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
