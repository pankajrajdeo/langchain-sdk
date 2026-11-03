---
title: "PGVector integration"
description: "Integrate with the PGVector vector store using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/vectorstores/pgvector"
category: "docs"
tags: [docs, integrations, vectorstores, pgvector]
---

# PGVector integration

> Integrate with the PGVector vector store using LangChain Python.

> An implementation of LangChain vectorstore abstraction using `postgres` as the backend and utilizing the `pgvector` extension.

The code lives in an integration package called: [langchain-postgres](https://github.com/langchain-ai/langchain-postgres/).

## Status

This code has been ported over from `langchain-community` into a dedicated package called `langchain-postgres`. The following changes have been made:

* `langchain-postgres` works only with psycopg3. Please update your connnecion strings from `postgresql+psycopg2://...` to `postgresql+psycopg://langchain:langchain@...` (yes, it's the driver name is `psycopg` not `psycopg3`, but it'll use `psycopg3`.
* The schema of the embedding store and collection have been changed to make add\_documents work correctly with user specified ids.
* One has to pass an explicit connection object now.

Currently, there is **no mechanism** that supports easy data migration on schema changes. Any schema changes in the vectorstore will require the user to recreate the tables and re-add the documents.
If this is a concern, please use a different vectorstore. If not, this implementation should be fine for your use case.

## Setup

First download the partner package:

```python
pip install -qU langchain-postgres
```

You can run the following command to spin up a postgres container with the `pgvector` extension:

```python
%docker run --name pgvector-container -e POSTGRES_USER=langchain -e POSTGRES_PASSWORD=langchain -e POSTGRES_DB=langchain -p 6024:5432 -d pgvector/pgvector:pg16
```

### Credentials

There are no credentials needed to run this notebook, just make sure you downloaded the `langchain-postgres` package and correctly started the postgres container.

If you want to get best in-class automated tracing of your model calls you can also set your [LangSmith](../../langsmith/observability.md) API key by uncommenting below:

```python
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
os.environ["LANGSMITH_TRACING"] = "true"
```

## Instantiation

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
from langchain_postgres import PGVector

# See docker command above to launch a postgres instance with pgvector enabled.
connection = "postgresql+psycopg://langchain:langchain@localhost:6024/langchain"  # Uses psycopg3!
collection_name = "my_docs"

vector_store = PGVector(
    embeddings=embeddings,
    collection_name=collection_name,
    connection=connection,
    use_jsonb=True,
)
```

## Manage vector store

### Add items to vector store

Note that adding documents by ID will over-write any existing documents that match that ID.

```python
from langchain_core.documents import Document

docs = [
    Document(
        page_content="there are cats in the pond",
        metadata={"id": 1, "location": "pond", "topic": "animals"},
    ),
    Document(
        page_content="ducks are also found in the pond",
        metadata={"id": 2, "location": "pond", "topic": "animals"},
    ),
    Document(
        page_content="fresh apples are available at the market",
        metadata={"id": 3, "location": "market", "topic": "food"},
    ),
    Document(
        page_content="the market also sells fresh oranges",
        metadata={"id": 4, "location": "market", "topic": "food"},
    ),
    Document(
        page_content="the new art exhibit is fascinating",
        metadata={"id": 5, "location": "museum", "topic": "art"},
    ),
    Document(
        page_content="a sculpture exhibit is also at the museum",
        metadata={"id": 6, "location": "museum", "topic": "art"},
    ),
    Document(
        page_content="a new coffee shop opened on Main Street",
        metadata={"id": 7, "location": "Main Street", "topic": "food"},
    ),
    Document(
        page_content="the book club meets at the library",
        metadata={"id": 8, "location": "library", "topic": "reading"},
    ),
    Document(
        page_content="the library hosts a weekly story time for kids",
        metadata={"id": 9, "location": "library", "topic": "reading"},
    ),
    Document(
        page_content="a cooking class for beginners is offered at the community center",
        metadata={"id": 10, "location": "community center", "topic": "classes"},
    ),
]

vector_store.add_documents(docs, ids=[doc.metadata["id"] for doc in docs])
```

```text
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

### Delete items from vector store

```python
vector_store.delete(ids=["3"])
```

## Query vector store

Once your vector store has been created and the relevant documents have been added you will most likely wish to query it during the running of your chain or agent.

### Filtering support

The vectorstore supports a set of filters that can be applied against the metadata fields of the documents.

| Operator | Meaning/Category |
| - | - |
| \$eq | Equality (==) |
| \$ne | Inequality (!=) |
| \$lt | Less than (\<) |
| \$lte | Less than or equal (\<=) |
| \$gt | Greater than (>) |
| \$gte | Greater than or equal (>=) |
| \$in | Special Cased (in) |
| \$nin | Special Cased (not in) |
| \$between | Special Cased (between) |
| \$like | Text (like) |
| \$ilike | Text (case-insensitive like) |
| \$and | Logical (and) |
| \$or | Logical (or) |

### Query directly

Performing a simple similarity search can be done as follows:

```python
results = vector_store.similarity_search(
    "kitty", k=10, filter={"id": {"$in": [1, 5, 2, 9]}}
)
for doc in results:
    print(f"* {doc.page_content} [{doc.metadata}]")
```

```text
* there are cats in the pond [{'id': 1, 'topic': 'animals', 'location': 'pond'}]
* the library hosts a weekly story time for kids [{'id': 9, 'topic': 'reading', 'location': 'library'}]
* ducks are also found in the pond [{'id': 2, 'topic': 'animals', 'location': 'pond'}]
* the new art exhibit is fascinating [{'id': 5, 'topic': 'art', 'location': 'museum'}]
```

If you provide a dict with multiple fields, but no operators, the top level will be interpreted as a logical **AND** filter

```python
vector_store.similarity_search(
    "ducks",
    k=10,
    filter={"id": {"$in": [1, 5, 2, 9]}, "location": {"$in": ["pond", "market"]}},
)
```

```text
[Document(metadata={'id': 1, 'topic': 'animals', 'location': 'pond'}, page_content='there are cats in the pond'),
 Document(metadata={'id': 2, 'topic': 'animals', 'location': 'pond'}, page_content='ducks are also found in the pond')]
```

```python
vector_store.similarity_search(
    "ducks",
    k=10,
    filter={
        "$and": [
            {"id": {"$in": [1, 5, 2, 9]}},
            {"location": {"$in": ["pond", "market"]}},
        ]
    },
)
```

```text
[Document(metadata={'id': 1, 'topic': 'animals', 'location': 'pond'}, page_content='there are cats in the pond'),
 Document(metadata={'id': 2, 'topic': 'animals', 'location': 'pond'}, page_content='ducks are also found in the pond')]
```

If you want to execute a similarity search and receive the corresponding scores you can run:

```python
results = vector_store.similarity_search_with_score(query="cats", k=1)
for doc, score in results:
    print(f"* [SIM={score:3f}] {doc.page_content} [{doc.metadata}]")
```

```text
* [SIM=0.763449] there are cats in the pond [{'id': 1, 'topic': 'animals', 'location': 'pond'}]
```

For a full list of the different searches you can execute on a `PGVector` vector store, please refer to the [API reference](https://reference.langchain.com/python/langchain-postgres/vectorstores/PGVector).

### Query by turning into retriever

You can also transform the vector store into a retriever for easier usage in your chains.

```python
retriever = vector_store.as_retriever(search_type="mmr", search_kwargs={"k": 1})
retriever.invoke("kitty")
```

```text
[Document(metadata={'id': 1, 'topic': 'animals', 'location': 'pond'}, page_content='there are cats in the pond')]
```

## Usage for retrieval-augmented generation

For guides on how to use this vector store for retrieval-augmented generation (RAG), see the following sections:

* [Retrieval docs](../../deepagents/retrieval.md)
* [Build a RAG app with LangChain](../../deepagents/rag.md)
* [Agentic RAG](../../langgraph/agentic-rag.md)

***

## API reference

For detailed documentation of all `PGVector` VectorStore features and configurations head to the [API reference](https://reference.langchain.com/python/langchain-postgres/vectorstores/PGVector).

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/vectorstores/pgvector.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
