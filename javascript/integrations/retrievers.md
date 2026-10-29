---
title: "Retriever integrations"
description: "Integrate with retrievers using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/retrievers"
category: "docs"
tags: [docs, javascript, integrations, retrievers]
---

# Retriever integrations

> Integrate with retrievers using LangChain JavaScript.

A [retriever](../deepagents/retrieval.md) is an interface that returns documents given an unstructured query.
It is more general than a vector store.
A retriever does not need to be able to store documents, only to return (or retrieve) them.

Retrievers accept a string query as input and return a list of `Document` objects.

For specifics on how to use retrievers, see the [relevant how-to guides here](../deepagents/retrieval.md).

Note that all [vector stores](vectorstores.md) can be [cast to retrievers](../deepagents/retrieval.md).
Refer to the vector store [integration docs](vectorstores.md) for available vector store retrievers.

## All retrievers

| Retriever | Self-host | Cloud offering | Package | Downloads |
| :- | :- | :- | :- | :- |
| [`AWSKendraRetriever`](retrievers/kendra-retriever.md) | | | [`@langchain/aws`](https://www.npmjs.com/package/@langchain/aws) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/aws?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/aws) |
| [`Knowledge bases for Amazon Bedrock`](retrievers/bedrock-knowledge-bases.md) | | | [`@langchain/aws`](https://www.npmjs.com/package/@langchain/aws) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/aws?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/aws) |
| [`ExaRetriever`](retrievers/exa.md) | | | [`@langchain/exa`](https://www.npmjs.com/package/@langchain/exa) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/exa?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/exa) |
| [`PerplexitySearchRetriever`](retrievers/perplexity_search.md) | | | [`@langchain/perplexity`](https://www.npmjs.com/package/@langchain/perplexity) | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/perplexity?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/perplexity) |
| [`SourceyRetriever`](retrievers/sourcey.md) | | | [`langchain-sourcey`](https://www.npmjs.com/package/langchain-sourcey) | [  ![Downloads per month](https://img.shields.io/npm/dm/langchain-sourcey?style=flat-square\&label=%20&)](https://www.npmjs.com/package/langchain-sourcey) |
| [`AlchemystRetriever`](https://getalchemystai.com/docs) | | | [`@alchemystai/langchain-js`](https://www.npmjs.com/package/@alchemystai/langchain-js) | [  ![Downloads per month](https://img.shields.io/npm/dm/@alchemystai/langchain-js?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@alchemystai/langchain-js) |
| [`FoxNoseRetriever`](https://foxnose.net/docs/integrations/langchain-js) | ❌ | ✅ | [`@foxnose/langchain`](https://www.npmjs.com/package/@foxnose/langchain) | [  ![Downloads per month](https://img.shields.io/npm/dm/@foxnose/langchain?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@foxnose/langchain) |
| [`RecallRetriever`](https://recallmem.dev/guides/langchain) | ✅ | ✅ | [`@recall-memory/langchain`](https://www.npmjs.com/package/@recall-memory/langchain) | [  ![Downloads per month](https://img.shields.io/npm/dm/@recall-memory/langchain?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@recall-memory/langchain) |
| [`Hyde`](retrievers/hyde.md) | | | | N/A |
| [`Self Querying with SAP HANA Cloud Vector Engine`](retrievers/self_query/hanavector_self_query.md) | | | | N/A |
| [`Time-weighted`](retrievers/time-weighted-retriever.md) | | | | N/A |

> [!NOTE]
>
> If you'd like to contribute an integration, see [Contributing integrations](../contributing.md#add-a-new-integration).

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/retrievers/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
