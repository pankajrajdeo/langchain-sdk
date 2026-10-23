---
title: "Store integrations"
description: "Integrate with stores using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/stores"
category: "docs"
tags: [docs, integrations, stores]
---

# Store integrations

> Integrate with stores using LangChain Python.

## Overview

LangChain provides a key-value store interface for storing and retrieving data by key. The key-value store interface in LangChain is primarily used for caching [embeddings](embeddings.md).

## Interface

All [`BaseStores`](https://reference.langchain.com/python/langchain-core/stores/BaseStore) support the following interface:

* `mget(key: Sequence[str]) -> List[Optional[bytes]]`: get the contents of multiple keys, returning `None` if the key does not exist
* `mset(key_value_pairs: Sequence[Tuple[str, bytes]]) -> None`: set the contents of multiple keys
* `mdelete(key: Sequence[str]) -> None`: delete multiple keys
* `yield_keys(prefix: Optional[str] = None) -> Iterator[str]`: yield all keys in the store, optionally filtering by a prefix

> [!NOTE]
>
> Base stores are designed to work **multiple** key-value pairs at once for efficiency. This saves on network round-trips and may allow for more efficient batch operations in the underlying store.

## Built-in stores for local development

> **[InMemoryByteStore](stores/in_memory.md)**

> **[LocalFileStore](stores/file_system.md)**

## Custom stores

You can also implement your own custom store by extending the [`BaseStore`](https://reference.langchain.com/python/langchain-core/stores/BaseStore) class. See the [store interface documentation](https://reference.langchain.com/python/langchain-core/stores/BaseStore) for more details.

## All key-value stores

| Integration | Downloads |
| :- | :- |
| [`AstraDBByteStore`](stores/astradb.md) | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-astradb/month)](https://pypi.org/project/langchain-astradb/) |
| [`ElasticsearchEmbeddingsCache`](stores/elasticsearch.md) | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-elasticsearch/month)](https://pypi.org/project/langchain-elasticsearch/) |
| [`M3Store`](https://github.com/skynetcmd/m3-memory/blob/main/docs/integrations/LANGCHAIN.md) | [  ![Downloads per month](https://static.pepy.tech/badge/m3-memory/month)](https://pypi.org/project/m3-memory/) |
| [`HindsightStore`](https://docs.hindsight.vectorize.io/sdks/integrations/langgraph) | [  ![Downloads per month](https://static.pepy.tech/badge/hindsight-langgraph/month)](https://pypi.org/project/hindsight-langgraph/) |
| [`OmemStore`](https://infrastructure.omem-cloud.com/docs) | [  ![Downloads per month](https://static.pepy.tech/badge/omem-infrastructure/month)](https://pypi.org/project/omem-infrastructure/) |
| [`PplStore`](https://github.com/ppl-crm/ppl-memory) | [  ![Downloads per month](https://static.pepy.tech/badge/ppl-memory/month)](https://pypi.org/project/ppl-memory/) |
| [`DynamoDBStore`](https://skamalj.github.io/agentstate-reducer/langgraph/stores/) | [  ![Downloads per month](https://static.pepy.tech/badge/langgraph-store-dynamodb/month)](https://pypi.org/project/langgraph-store-dynamodb/) |
| [`LithtrixStore`](https://docs.lithtrix.ai/integrations/langgraph) | [  ![Downloads per month](https://static.pepy.tech/badge/lithtrix-langgraph/month)](https://pypi.org/project/lithtrix-langgraph/) |
| [`BigtableByteStore`](stores/bigtable.md) | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-google-bigtable/month)](https://pypi.org/project/langchain-google-bigtable/) |
| [`PostgresStore`](https://skamalj.github.io/agentstate-reducer/langgraph/stores/) | [  ![Downloads per month](https://static.pepy.tech/badge/langgraph-store-postgres/month)](https://pypi.org/project/langgraph-store-postgres/) |
| [`XNSByteStore`](https://docs.xns.tech) | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-xns/month)](https://pypi.org/project/langchain-xns/) |
| [`CosmosDBStore`](https://skamalj.github.io/agentstate-reducer/langgraph/stores/) | [  ![Downloads per month](https://static.pepy.tech/badge/langgraph-store-cosmosdb/month)](https://pypi.org/project/langgraph-store-cosmosdb/) |
| [`FirestoreStore`](https://skamalj.github.io/agentstate-reducer/langgraph/stores/) | [  ![Downloads per month](https://static.pepy.tech/badge/langgraph-store-firestore/month)](https://pypi.org/project/langgraph-store-firestore/) |
| [`GridGainCheckpointSaver`](https://pypi.org/project/langgraph-checkpoint-gridgain/) | [  ![Downloads per month](https://static.pepy.tech/badge/langgraph-checkpoint-gridgain/month)](https://pypi.org/project/langgraph-checkpoint-gridgain/) |
| [`QdrantStore`](https://pypi.org/project/langgraph-store-qdrant/) | [  ![Downloads per month](https://static.pepy.tech/badge/langgraph-store-qdrant/month)](https://pypi.org/project/langgraph-store-qdrant/) |
| [`InspeximusStore`](https://dancenitra.github.io/inspeximus/) | [  ![Downloads per month](https://static.pepy.tech/badge/langgraph-store-inspeximus/month)](https://pypi.org/project/langgraph-store-inspeximus/) |
| [`UpstashStore`](https://github.com/Tghez/langgraph-store-upstash) | [  ![Downloads per month](https://static.pepy.tech/badge/langgraph-store-upstash/month)](https://pypi.org/project/langgraph-store-upstash/) |
| [`TypeDBStore`](https://typedb.com/docs) | [  ![Downloads per month](https://static.pepy.tech/badge/langgraph-store-typedb/month)](https://pypi.org/project/langgraph-store-typedb/) |
| [`InMemoryByteStore`](stores/in_memory.md) | N/A |
| [`LocalFileStore`](stores/file_system.md) | N/A |

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/stores/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
