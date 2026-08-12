> ## Documentation Index
> Fetch the complete documentation index at: https://docs.langchain.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Elasticsearch integrations

> Integrate with Elasticsearch using LangChain Python.

> [Elasticsearch](https://www.elastic.co/elasticsearch/) is a distributed, RESTful search and analytics engine.
> It provides a distributed, multi-tenant-capable full-text search engine with an HTTP web interface and schema-free
> JSON documents.

## Installation and setup

### Setup Elasticsearch

There are two ways to get started with Elasticsearch:

#### Install Elasticsearch on your local machine

The easiest way to run Elasticsearch locally for development and testing is using the [start-local](https://github.com/elastic/start-local) script. This script sets up Elasticsearch using Docker with a simple one-line command.

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -fsSL https://elastic.co/start-local | sh
```

This creates an `elastic-start-local` folder. To start Elasticsearch:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
cd elastic-start-local
./start.sh
```

Elasticsearch will be available at `http://localhost:9200`. The password for the `elastic` user and API key are automatically generated and stored in the `.env` file in the `elastic-start-local` folder.

If you only need Elasticsearch without Kibana, you can use the `--esonly` option:

```bash theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
curl -fsSL https://elastic.co/start-local | sh -s -- --esonly
```

<Note>
  The start-local setup is for local testing only and should not be used in production. For production installations, refer to the official [Elasticsearch documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html).
</Note>

#### Deploy Elasticsearch on elastic cloud

`Elastic Cloud` is a managed Elasticsearch service. Signup for a [free trial](https://cloud.elastic.co/registration?utm_source=langchain\&utm_content=documentation).

### Install client

<CodeGroup>
  ```bash pip theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  pip install elasticsearch
  pip install langchain-elasticsearch
  ```

  ```bash uv theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
  uv add elasticsearch
  uv add langchain-elasticsearch
  ```
</CodeGroup>

## Embedding models

See a [usage example](/oss/python/integrations/embeddings/elasticsearch).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_elasticsearch import ElasticsearchEmbeddings
```

## Vector store

See a [usage example](/oss/python/integrations/vectorstores/elasticsearch).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_elasticsearch import ElasticsearchStore
```

## Retrievers

### ElasticsearchRetriever

The `ElasticsearchRetriever` enables flexible access to all Elasticsearch features
through the Query DSL.

See a [usage example](/oss/python/integrations/retrievers/elasticsearch_retriever).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_elasticsearch import ElasticsearchRetriever
```

## LLM cache

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_elasticsearch import ElasticsearchCache
```

## Byte store

See a [usage example](/oss/python/integrations/stores/elasticsearch).

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_elasticsearch import ElasticsearchEmbeddingsCache
```

## Chain

It is a chain for interacting with Elasticsearch Database.

```python theme={"theme":{"light":"catppuccin-latte","dark":"catppuccin-mocha"}}
from langchain_classic.chains.elasticsearch_database import ElasticsearchDatabaseChain
```

***

<div className="source-links">
  <Callout icon="terminal-2">
    [Connect these docs](/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.
  </Callout>

  <Callout icon="edit">
    [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/providers/elasticsearch.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
  </Callout>
</div>
