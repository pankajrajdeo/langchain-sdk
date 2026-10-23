---
title: "Embedding model integrations"
description: "Integrate with embedding models using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/embeddings"
category: "docs"
tags: [docs, javascript, integrations, embeddings]
---

# Embedding model integrations

> Integrate with embedding models using LangChain JavaScript.

## Overview

> [!NOTE]
>
> This overview covers **text-based embedding models**. LangChain does not currently support multimodal embeddings.

Embedding models transform raw text—such as a sentence, paragraph, or tweet—into a fixed-length vector of numbers that captures its **semantic meaning**. These vectors allow machines to compare and search text based on meaning rather than exact words.

In practice, this means that texts with similar ideas are placed close together in the vector space. For example, instead of matching only the phrase *"machine learning"*, embeddings can surface documents that discuss related concepts even when different wording is used.

### How it works

1. **Vectorization**: The model encodes each input string as a high-dimensional vector.
2. **Similarity scoring**: Vectors are compared using mathematical metrics to measure how closely related the underlying texts are.

### Similarity metrics

Several metrics are commonly used to compare embeddings:

* **Cosine similarity**: measures the angle between two vectors.
* **Euclidean distance**: measures the straight-line distance between points.
* **Dot product**: measures how much one vector projects onto another.

## Interface

LangChain provides a standard interface for text embedding models (e.g., OpenAI, Cohere, Hugging Face) via the [Embeddings](https://reference.langchain.com/javascript/langchain-core/embeddings/Embeddings) interface.

Two main methods are available:

* `embedDocuments(documents: string[]) → number[][]`: Embeds a list of documents.
* `embedQuery(text: string) → number[]`: Embeds a single query.

> [!NOTE]
>
> The interface allows queries and documents to be embedded with different strategies, though most providers handle them the same way in practice.

## Install and use

> **OpenAI**
>
> Install dependencies:
>
**npm**

```bash
> npm install @langchain/openai @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/openai @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/openai @langchain/core
```
>
> Add environment variables:
>
```bash
> OPENAI_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { OpenAIEmbeddings } from "@langchain/openai";
>
> const embeddings = new OpenAIEmbeddings({
>   model: "text-embedding-3-large"
> });
```

> **Azure**
>
> Install dependencies
>
**npm**

```bash
> npm install @langchain/openai @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/openai @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/openai @langchain/core
```
>
> Add environment variables:
>
```bash
> AZURE_OPENAI_API_INSTANCE_NAME=<YOUR_INSTANCE_NAME>
> AZURE_OPENAI_API_KEY=<YOUR_KEY>
> AZURE_OPENAI_API_VERSION="2024-02-01"
```
>
> Instantiate the model:
>
```typescript
> import { AzureOpenAIEmbeddings } from "@langchain/openai";
>
> const embeddings = new AzureOpenAIEmbeddings({
>   azureOpenAIApiEmbeddingsDeploymentName: "text-embedding-ada-002"
> });
```

> **AWS**
>
> Install dependencies:
>
**npm**

```bash
> npm install @langchain/aws @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/aws @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/aws @langchain/core
```
>
> Add environment variables:
>
```bash
> BEDROCK_AWS_REGION=your-region
```
>
> Instantiate the model:
>
```typescript
> import { BedrockEmbeddings } from "@langchain/aws";
>
> const embeddings = new BedrockEmbeddings({
>   model: "amazon.titan-embed-text-v1"
> });
```

> **Google Gemini**
>
> Install dependencies:
>
**npm**

```bash
> npm install @langchain/google-genai @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/google-genai @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/google-genai @langchain/core
```
>
> Add environment variables:
>
```bash
> GOOGLE_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { GoogleGenerativeAIEmbeddings } from "@langchain/google-genai";
>
> const embeddings = new GoogleGenerativeAIEmbeddings({
>   model: "gemini-embedding-001"
> });
```

> **Gemini Enterprise Agent Platform**
>
> Install dependencies:
>
**npm**

```bash
> npm install @langchain/google-vertexai @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/google-vertexai @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/google-vertexai @langchain/core
```
>
> Add environment variables:
>
```bash
> GOOGLE_APPLICATION_CREDENTIALS=credentials.json
```
>
> Instantiate the model:
>
```typescript
> import { VertexAIEmbeddings } from "@langchain/google-vertexai";
>
> const embeddings = new VertexAIEmbeddings({
>   model: "gemini-embedding-001"
> });
```

> **MistralAI**
>
> Install dependencies:
>
**npm**

```bash
> npm install @langchain/mistralai @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/mistralai @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/mistralai @langchain/core
```
>
> Add environment variables:
>
```bash
> MISTRAL_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { MistralAIEmbeddings } from "@langchain/mistralai";
>
> const embeddings = new MistralAIEmbeddings({
>   model: "mistral-embed"
> });
```

> **Cohere**
>
> Install dependencies:
>
**npm**

```bash
> npm install @langchain/cohere @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/cohere @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/cohere @langchain/core
```
>
> Add environment variables:
>
```bash
> COHERE_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { CohereEmbeddings } from "@langchain/cohere";
>
> const embeddings = new CohereEmbeddings({
>   model: "embed-english-v3.0"
> });
```

> **Ollama**
>
> Install dependencies:
>
**npm**

```bash
> npm install @langchain/ollama @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/ollama @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/ollama @langchain/core
```
>
> Instantiate the model:
>
```typescript
> import { OllamaEmbeddings } from "@langchain/ollama";
>
> const embeddings = new OllamaEmbeddings({
>   model: "llama2",
>   baseUrl: "http://localhost:11434", // Default value
> });
```

> **Voyage AI**
>
> Install dependencies:
>
**npm**

```bash
> npm install @langchain/mongodb @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/mongodb @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/mongodb @langchain/core
```
>
> Add environment variables:
>
```bash
> VOYAGE_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { VoyageEmbeddings } from "@langchain/mongodb";
>
> const embeddings = new VoyageEmbeddings({
>   model: "voyage-4"
> });
```

## Caching

Embeddings can be stored or temporarily cached to avoid needing to recompute them.

Caching embeddings can be done using a `CacheBackedEmbeddings`. This wrapper stores embeddings in a key-value store, where the text is hashed and the hash is used as the key in the cache.

The main supported way to initialize a `CacheBackedEmbeddings` is `fromBytesStore`. It takes the following parameters:

* **underlyingEmbeddings**: The embedder to use for embedding.
* **documentEmbeddingStore**: Any [`BaseStore`](stores.md) for caching document embeddings.
* **options.namespace**: (optional, defaults to `""`) The namespace to use for the document cache. Helps avoid collisions (e.g., set it to the embedding model name).

- Always set the `namespace` parameter to avoid collisions when using different embedding models.
- `CacheBackedEmbeddings` does not cache query embeddings by default. To enable this, specify a `query_embedding_store`.

```typescript
import { CacheBackedEmbeddings } from "@langchain/classic/embeddings/cache_backed";
import { InMemoryStore } from "@langchain/core/stores";

const underlyingEmbeddings = new OpenAIEmbeddings();

const inMemoryStore = new InMemoryStore();

const cacheBackedEmbeddings = CacheBackedEmbeddings.fromBytesStore(
  underlyingEmbeddings,
  inMemoryStore,
  {
    namespace: underlyingEmbeddings.model,
  }
);

// Example: caching a query embedding
const tic = Date.now();
const queryEmbedding = cacheBackedEmbeddings.embedQuery("Hello, world!");
console.log(`First call took: ${Date.now() - tic}ms`);

// Example: caching a document embedding
const tic = Date.now();
const documentEmbedding = cacheBackedEmbeddings.embedDocuments(["Hello, world!"]);
console.log(`Cached creation time: ${Date.now() - tic}ms`);
```

In production, you would typically use a more robust persistent store, such as a database or cloud storage. Please see [stores integrations](stores.md) for options.

## All integrations

| Integration | Downloads |
| :- | :- |
| [`AzureOpenAIEmbeddings`](embeddings/azure_openai.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/openai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/openai) |
| [`OpenAIEmbeddings`](embeddings/openai.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/openai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/openai) |
| [`Bedrock`](embeddings/bedrock.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/aws?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/aws) |
| [`GoogleGenerativeAIEmbeddings`](embeddings/google_generative_ai.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/google-genai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/google-genai) |
| [`VertexAIEmbeddings`](embeddings/google_vertex_ai.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/google-vertexai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/google-vertexai) |
| [`OllamaEmbeddings`](embeddings/ollama.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/ollama?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/ollama) |
| [`MistralAIEmbeddings`](embeddings/mistralai.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/mistralai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/mistralai) |
| [`PineconeEmbeddings`](embeddings/pinecone.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/pinecone?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/pinecone) |
| [`VoyageEmbeddings`](embeddings/voyageai.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/mongodb?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/mongodb) |
| [`CohereEmbeddings`](embeddings/cohere.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/cohere?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/cohere) |
| [`Baidu qianfan`](embeddings/baidu_qianfan.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/baidu-qianfan?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/baidu-qianfan) |
| [`Nomic`](embeddings/nomic.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/nomic?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/nomic) |
| [`CloudflareWorkersAIEmbeddings`](embeddings/cloudflare_ai.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/cloudflare?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/cloudflare) |
| [`FireworksEmbeddings`](embeddings/fireworks.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/fireworks?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/fireworks) |
| [`WatsonxEmbeddings`](embeddings/ibm.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/ibm?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/ibm) |
| [`TogetherAIEmbeddings`](embeddings/togetherai.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/together-ai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/together-ai) |
| [`Mixedbread AI`](embeddings/mixedbread_ai.md) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/mixedbread-ai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/mixedbread-ai) |
| [`SCXEmbeddings`](https://scx.ai/) | [  ![Downloads per month](https://img.shields.io/npm/dm/@scx-ai/langchain?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@scx-ai/langchain) |
| [`Minimax`](embeddings/minimax.md) | N/A |
| [`OracleEmbeddings`](embeddings/oracleai.md) | N/A |

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/embeddings/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
