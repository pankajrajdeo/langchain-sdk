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
> Base stores are designed to work **multiple** key-value pairs at once for efficiency. This saves on network round-trips and may allow for more efficient batch operations in the underlying store.

## Built-in stores for local development

#### [InMemoryByteStore](stores/in_memory.md)

#### [LocalFileStore](stores/file_system.md)

## Custom stores

You can also implement your own custom store by extending the [`BaseStore`](https://reference.langchain.com/python/langchain-core/stores/BaseStore) class. See the [store interface documentation](https://reference.langchain.com/python/langchain-core/stores/BaseStore) for more details.

## All key-value stores

| Integration                                                                                  | Downloads                                                                                                                                                                                                                                                        |
| :------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [`ElasticsearchEmbeddingsCache`](stores/elasticsearch.md)              | <span data-sort-value="238000"><a href="https://pypi.org/project/langchain-elasticsearch/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-elasticsearch/month" alt="Downloads per month" class="rounded not-prose" /></a></span>    |
| [`AstraDBByteStore`](stores/astradb.md)                                | <span data-sort-value="189000"><a href="https://pypi.org/project/langchain-astradb/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-astradb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                |
| [`M3Store`](https://github.com/skynetcmd/m3-memory/blob/main/docs/integrations/LANGCHAIN.md) | <span data-sort-value="24000"><a href="https://pypi.org/project/m3-memory/" target="_blank">  <img src="https://static.pepy.tech/badge/m3-memory/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                                 |
| [`OmemStore`](https://infrastructure.omem-cloud.com/docs)                                    | <span data-sort-value="10000"><a href="https://pypi.org/project/omem-infrastructure/" target="_blank">  <img src="https://static.pepy.tech/badge/omem-infrastructure/month" alt="Downloads per month" class="rounded not-prose" /></a></span>             |
| [`LithtrixStore`](https://docs.lithtrix.ai/integrations/langgraph)                           | <span data-sort-value="3000"><a href="https://pypi.org/project/lithtrix-langgraph/" target="_blank">  <img src="https://static.pepy.tech/badge/lithtrix-langgraph/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                |
| [`HindsightStore`](https://docs.hindsight.vectorize.io/sdks/integrations/langgraph)          | <span data-sort-value="1000"><a href="https://pypi.org/project/hindsight-langgraph/" target="_blank">  <img src="https://static.pepy.tech/badge/hindsight-langgraph/month" alt="Downloads per month" class="rounded not-prose" /></a></span>              |
| [`BigtableByteStore`](stores/bigtable.md)                              | <span data-sort-value="503"><a href="https://pypi.org/project/langchain-google-bigtable/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-google-bigtable/month" alt="Downloads per month" class="rounded not-prose" /></a></span>   |
| [`UpstashStore`](https://github.com/Tghez/langgraph-store-upstash)                           | <span data-sort-value="472"><a href="https://pypi.org/project/langgraph-store-upstash/" target="_blank">  <img src="https://static.pepy.tech/badge/langgraph-store-upstash/month" alt="Downloads per month" class="rounded not-prose" /></a></span>       |
| [`XNSByteStore`](https://docs.xns.tech)                                                      | <span data-sort-value="402"><a href="https://pypi.org/project/langchain-xns/" target="_blank">  <img src="https://static.pepy.tech/badge/langchain-xns/month" alt="Downloads per month" class="rounded not-prose" /></a></span>                           |
| [`InspeximusStore`](https://dancenitra.github.io/inspeximus/)                                | <span data-sort-value="130"><a href="https://pypi.org/project/langgraph-store-inspeximus/" target="_blank">  <img src="https://static.pepy.tech/badge/langgraph-store-inspeximus/month" alt="Downloads per month" class="rounded not-prose" /></a></span> |
| [`TypeDBStore`](https://typedb.com/docs)                                                     | <span data-sort-value="59"><a href="https://pypi.org/project/langgraph-store-typedb/" target="_blank">  <img src="https://static.pepy.tech/badge/langgraph-store-typedb/month" alt="Downloads per month" class="rounded not-prose" /></a></span>          |
| [`InMemoryByteStore`](stores/in_memory.md)                             | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                            |
| [`LocalFileStore`](stores/file_system.md)                              | <span data-sort-value="-1">N/A</span>                                                                                                                                                                                                                            |

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/stores/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
