# Google integrations
> Source: [Original LangChain documentation](https://docs.langchain.com/oss/python/integrations/providers/google)
Integrate with Google using LangChain Python.

This page covers all LangChain integrations with [Google Gemini](https://ai.google.dev/gemini-api/docs), [Google Cloud](https://cloud.google.com/), and other Google products (such as Google Maps, YouTube, and [more](https://docs.langchain.com/oss/python/integrations/providers/google#other-google-products)).

> [!NOTE]
> **Unified SDK & package consolidation**
>
> As of `langchain-google-genai` 4.0.0, this package uses the consolidated [`google-genai`](https://googleapis.github.io/python-genai/) SDK and now supports **both the Gemini Developer API and Vertex AI** backends.
>
> The `langchain-google-vertexai` package remains supported for Vertex AI platform-specific features (Model Garden, Vector Search, evaluation services, etc.).
>
> Read the [full announcement and migration guide](https://github.com/langchain-ai/langchain-google/discussions/1422).

Not sure which package to use?

<details>
<summary>Google Generative AI (Gemini API & Vertex AI)</summary>

Access Google Gemini models via the **[Gemini Developer API](https://ai.google.dev/)** or **[Vertex AI](https://cloud.google.com/vertex-ai)**. The backend is selected automatically based on your configuration.

* **Gemini Developer API**: Quick setup with API key, ideal for individual developers and rapid prototyping
* **Vertex AI**: Enterprise features with Google Cloud integration (requires GCP project)

Use the `langchain-google-genai` package for chat models, LLMs, and embeddings.

[See integrations.](https://docs.langchain.com/oss/python/integrations/providers/google#google-generative-ai)

</details>

<details>
<summary>Google Cloud (Vertex AI Platform Services)</summary>

Access Vertex AI platform-specific services beyond Gemini models: Model Garden (Llama, Mistral, Anthropic), evaluation services, and specialized vision models.

Use the `langchain-google-vertexai` package for platform services and specific packages (e.g., `langchain-google-community`, `langchain-google-cloud-sql-pg`) for other cloud services like databases and storage.

[See integrations.](https://docs.langchain.com/oss/python/integrations/providers/google#google-cloud)

</details>

See Google's guide on [migrating from the Gemini API to Vertex AI](https://ai.google.dev/gemini-api/docs/migrate-to-cloud) for more details on the differences.

***

## Google Generative AI

Access Google Gemini models via the [Gemini Developer API](https://ai.google.dev/gemini-api/docs) or [Vertex AI](https://cloud.google.com/vertex-ai) using the unified `langchain-google-genai` package.

### Chat models

#### [ChatGoogleGenerativeAI](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai)
Google Gemini chat models via **Gemini Developer API** or **Vertex AI**.

### LLMs

#### [GoogleGenerativeAI](https://docs.langchain.com/oss/python/integrations/llms/google_generative_ai)
Gemini models using the (legacy) LLM text completion interface.

### Embedding models

#### [GoogleGenerativeAIEmbeddings](https://docs.langchain.com/oss/python/integrations/embeddings/google_generative_ai)
Gemini embedding models via **Gemini Developer API** or **Vertex AI**.

***

## Google Cloud

Access Vertex AI platform-specific services including Model Garden (Llama, Mistral, Anthropic), Vector Search, evaluation services, and specialized vision models.

> [!NOTE]
> **For Gemini models**, use [`ChatGoogleGenerativeAI`](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai) from `langchain-google-genai`. The classes below focus on **Vertex AI platform services** not available in the consolidated SDK.

### Chat models

#### [ChatAnthropicVertex](https://docs.langchain.com/oss/python/integrations/chat/google_anthropic_vertex)
Anthropic on Vertex AI Model Garden

<details>
<summary>ChatVertexAI (deprecated)</summary>

**Deprecated**—Use [`ChatGoogleGenerativeAI`](https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai) for Gemini models instead.

```python
from langchain_google_vertexai import ChatVertexAI
```

</details>

<details>
<summary>VertexModelGardenLlama</summary>

Llama on Vertex AI Model Garden

```python
from langchain_google_vertexai.model_garden_maas.llama import VertexModelGardenLlama
```

</details>

<details>
<summary>VertexModelGardenMistral</summary>

Mistral on Vertex AI Model Garden

```python
from langchain_google_vertexai.model_garden_maas.mistral import VertexModelGardenMistral
```

</details>

<details>
<summary>GemmaChatLocalHF</summary>

Local Gemma model loaded from HuggingFace.

```python
from langchain_google_vertexai.gemma import GemmaChatLocalHF
```

</details>

<details>
<summary>GemmaChatLocalKaggle</summary>

Local Gemma model loaded from Kaggle.

```python
from langchain_google_vertexai.gemma import GemmaChatLocalKaggle
```

</details>

<details>
<summary>GemmaChatVertexAIModelGarden</summary>

Gemma on Vertex AI Model Garden

```python
from langchain_google_vertexai.gemma import GemmaChatVertexAIModelGarden
```

</details>

<details>
<summary>VertexAIImageCaptioningChat</summary>

Image captioning model as a chat interface.

```python
from langchain_google_vertexai.vision_models import VertexAIImageCaptioningChat
```

</details>

<details>
<summary>VertexAIImageEditorChat</summary>

Edit images given a prompt. Currently supports mask-free editing only.

```python
from langchain_google_vertexai.vision_models import VertexAIImageEditorChat
```

</details>

<details>
<summary>VertexAIImageGeneratorChat</summary>

Generate images from a prompt.

```python
from langchain_google_vertexai.vision_models import VertexAIImageGeneratorChat
```

</details>

<details>
<summary>VertexAIVisualQnAChat</summary>

Visual question answering model as a chat interface.

```python
from langchain_google_vertexai.vision_models import VertexAIVisualQnAChat
```

</details>

### LLMs

(Legacy) string-in, string-out LLM interface.

#### [VertexAIModelGarden](https://docs.langchain.com/oss/python/integrations/llms/google_vertex_ai#vertex-model-garden)
Hundreds of OSS models via Vertex AI Model Garden.

<details>
<summary>VertexAI (deprecated)</summary>

**Deprecated**—Use [`GoogleGenerativeAI`](https://docs.langchain.com/oss/python/integrations/llms/google_generative_ai) for Gemini models instead.

```python
from langchain_google_vertexai import VertexAI
```

</details>

<details>
<summary>Gemma local from Hugging Face</summary>

Local Gemma model loaded from HuggingFace.

```python
from langchain_google_vertexai.gemma import GemmaLocalHF
```

</details>

<details>
<summary>Gemma local from Kaggle</summary>

Local Gemma model loaded from Kaggle.

```python
from langchain_google_vertexai.gemma import GemmaLocalKaggle
```

</details>

<details>
<summary>Gemma on Vertex AI Model Garden</summary>

```python
from langchain_google_vertexai.gemma import GemmaVertexAIModelGarden
```

</details>

<details>
<summary>Vertex AI image captioning</summary>

Image captioning model as an LLM interface.

```python
from langchain_google_vertexai.vision_models import VertexAIImageCaptioning
```

</details>

### Embedding models

<details>
<summary>VertexAIEmbeddings (deprecated)</summary>

**Deprecated**—Use [`GoogleGenerativeAIEmbeddings`](https://docs.langchain.com/oss/python/integrations/embeddings/google_generative_ai) instead.

```python
from langchain_google_vertexai import VertexAIEmbeddings
```

</details>

### Document loaders

#### [AlloyDB for PostgreSQL](https://docs.langchain.com/oss/python/integrations/document_loaders/google_alloydb)
PostgreSQL-compatible database on Google Cloud.

#### [BigQuery](https://docs.langchain.com/oss/python/integrations/document_loaders/google_bigquery)
Serverless data warehouse.

#### [Bigtable](https://docs.langchain.com/oss/python/integrations/document_loaders/google_bigtable)
Key-value and wide-column store for structured and semi-structured data.

#### [Cloud SQL for MySQL](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_sql_mysql)
Managed MySQL database.

#### [Cloud SQL for SQL Server](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_sql_mssql)
Managed SQL Server database.

#### [Cloud SQL for PostgreSQL](https://cloud.google.com/sql/docs/postgres)
Managed PostgreSQL database.

#### [Cloud Storage (directory)](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_storage_directory)
Load documents from a GCS bucket directory.

#### [Cloud Storage (file)](https://docs.langchain.com/oss/python/integrations/document_loaders/google_cloud_storage_file)
Load a single document from GCS.

#### [El Carro for Oracle Workloads](https://github.com/googleapis/langchain-google-el-carro-python/)
Oracle databases on Kubernetes via El Carro.

#### [Firestore (Native Mode)](https://docs.langchain.com/oss/python/integrations/document_loaders/google_firestore)
NoSQL document database.

#### [Firestore (Datastore Mode)](https://docs.langchain.com/oss/python/integrations/document_loaders/google_datastore)
Firestore in Datastore mode.

#### [Memorystore for Redis](https://docs.langchain.com/oss/python/integrations/document_loaders/google_memorystore_redis)
Managed Redis service.

#### [Spanner](https://docs.langchain.com/oss/python/integrations/document_loaders/google_spanner)
Globally distributed relational database.

#### [Speech-to-Text](https://docs.langchain.com/oss/python/integrations/document_loaders/google_speech_to_text)
Transcribe audio files.

<details>
<summary>Cloud Vision loader</summary>

Load data using Google Cloud Vision API.

```python
from langchain_google_community.vision import CloudVisionLoader
```

</details>

### Document transformers

#### [Document AI](https://docs.langchain.com/oss/python/integrations/document_transformers/google_docai)
Extract structured data from unstructured documents.

#### [Google Translate](https://docs.langchain.com/oss/python/integrations/document_transformers/google_translate)
Translate text and HTML via Cloud Translation API.

### Vector stores

Store and search vectors using Google Cloud databases and Vertex AI Vector Search.

#### [AlloyDB for PostgreSQL](https://docs.langchain.com/oss/python/integrations/vectorstores/google_alloydb)
PostgreSQL-compatible vector store on AlloyDB.

#### [BigQuery Vector Search](https://docs.langchain.com/oss/python/integrations/vectorstores/google_bigquery_vector_search)
Semantic search using GoogleSQL with vector indexes.

#### [Memorystore for Redis](https://docs.langchain.com/oss/python/integrations/vectorstores/google_memorystore_redis)
Vector store on Memorystore for Redis.

#### [Spanner](https://docs.langchain.com/oss/python/integrations/vectorstores/google_spanner)
Vector store on Cloud Spanner.

#### [Bigtable](https://cloud.google.com/bigtable)
Vector store on Cloud Bigtable.

#### [Firestore (Native Mode)](https://docs.langchain.com/oss/python/integrations/vectorstores/google_firestore)
Vector store on Firestore.

#### [Cloud SQL for MySQL](https://docs.langchain.com/oss/python/integrations/vectorstores/google_cloud_sql_mysql)
Vector store on Cloud SQL for MySQL.

#### [Cloud SQL for PostgreSQL](https://docs.langchain.com/oss/python/integrations/vectorstores/google_cloud_sql_pg)
Vector store on Cloud SQL for PostgreSQL.

#### [Vertex AI Vector Search](https://docs.langchain.com/oss/python/integrations/vectorstores/google_vertex_ai_vector_search)
Formerly known as Vertex AI Matching Engine, provides a low latency vector database. These vector databases are commonly referred to as vector similarity-matching or an approximate nearest neighbor (ANN) service.

#### [Vertex AI Vector Search + Datastore](https://docs.langchain.com/oss/python/integrations/vectorstores/google_vertex_ai_vector_search#optional--you-can-also-create-vector-and-store-chunks-in-a-datastore)
Vector search with Datastore for document storage.

### Retrievers

#### [Vertex AI Search](https://docs.langchain.com/oss/python/integrations/retrievers/google_vertex_ai_search)
Generative AI powered search via Vertex AI Search.

#### [Document AI Warehouse](https://cloud.google.com/document-ai-warehouse)
Search, store, and manage documents using Document AI Warehouse.

```python
from langchain_google_community import VertexAIMultiTurnSearchRetriever
from langchain_google_community import VertexAISearchRetriever
from langchain_google_community import VertexAISearchSummaryTool
```

### Tools

Integrate agents with various Google Cloud services.

#### [Text-to-Speech](https://docs.langchain.com/oss/python/integrations/tools/google_cloud_texttospeech)
Synthesize natural-sounding speech with 100+ voices.

### Callbacks

Track LLM/Chat model usage.

<details>
<summary>Vertex AI callback handler</summary>

Track `VertexAI` usage info.

```python
from langchain_google_vertexai.callbacks import VertexAICallbackHandler
```

</details>

<details>
<summary>Google BigQuery</summary>

See the [documentation](https://docs.langchain.com/oss/python/integrations/callbacks/google_bigquery) for more details.

```python
from langchain_google_community.callbacks.bigquery_callback import BigQueryCallbackHandler
```

</details>

### Evaluators

Evaluate model outputs using Vertex AI.

<details>
<summary>VertexPairWiseStringEvaluator</summary>

Pair-wise evaluation using Vertex AI models.

```python
from langchain_google_vertexai.evaluators.evaluation import VertexPairWiseStringEvaluator
```

</details>

<details>
<summary>VertexStringEvaluator</summary>

Single prediction evaluation using Vertex AI models.

```python
from langchain_google_vertexai.evaluators.evaluation import VertexStringEvaluator
```

</details>

***

## Other Google products

Integrations with various Google services beyond the core Cloud Platform.

### Document loaders

#### [Google Drive](https://docs.langchain.com/oss/python/integrations/document_loaders/google_drive)
Load files from Google Drive. Currently supports Google Docs.

### Retrievers

#### [Google Drive](https://docs.langchain.com/oss/python/integrations/retrievers/google_drive)
Retrieve documents from Google Drive.

### Tools

#### [Google Search](https://docs.langchain.com/oss/python/integrations/tools/google_search)
Web search via Google Custom Search Engine (CSE).

#### [Google Drive](https://docs.langchain.com/oss/python/integrations/tools/google_drive)
Interact with Google Drive.

### MCP

#### [MCP Toolbox](https://docs.langchain.com/oss/python/integrations/tools/mcp_toolbox)
Connect to databases including Cloud SQL and AlloyDB.

### Toolkits

#### [Gmail](https://docs.langchain.com/oss/python/integrations/tools/google_gmail)
Create, search, and send emails via the Gmail API.

***

## 3rd party integrations

Access Google services via unofficial third-party APIs.

### Search

#### [cloro](https://docs.cloro.dev)
Google Search results with AI Overview support.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/google.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
