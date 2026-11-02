---
title: "OpenVikingStore integration"
description: "Integrate with the OpenVikingStore store using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/stores/openviking"
category: "docs"
tags: [docs, integrations, stores, openviking]
---

# OpenVikingStore integration

> Integrate with the OpenVikingStore store using LangChain Python.

`OpenVikingStore` is a LangGraph [`BaseStore`](https://reference.langchain.com/python/langgraph.store/base/BaseStore) backed by OpenViking. Use it for [long-term memory](../../langgraph/stores.md) across threads in an OpenViking HTTP deployment.

## Overview

OpenViking is a context database for AI agents. The `langchain-openviking` package includes an `OpenVikingStore` class for storing LangGraph values as durable OpenViking content records and indexing them for query-based `search` calls.

This page documents the published `langchain-openviking` package on PyPI (v0.1.0).

### Integration details

| Class | Package | Local | JS support | Package downloads | Package latest |
| :- | :- | :-: | :-: | :-: | :-: |
| [`OpenVikingStore`](https://github.com/volcengine/OpenViking/blob/langchain-openviking@0.1.0/integrations/langchain/src/langchain_openviking/store.py) | [`langchain-openviking`](https://pypi.org/project/langchain-openviking/) | ❌ | ❌ | ![PyPI - Downloads](https://img.shields.io/pypi/dm/langchain-openviking?style=flat-square\&label=%20) | ![PyPI - Version](https://img.shields.io/pypi/v/langchain-openviking?style=flat-square\&label=%20) |

## Setup

To use `OpenVikingStore`, you need an OpenViking HTTP deployment and an API key.

### Installation

Install the integration with the `langgraph` extra:

```bash
pip install -qU "langchain-openviking[langgraph]"
```

### Credentials

Set your OpenViking URL and API key:

```python
from getpass import getpass

OPENVIKING_URL = getpass("OpenViking URL: ")
OPENVIKING_API_KEY = getpass("OpenViking API key: ")
```

## Instantiation

Instantiate `OpenVikingStore` with your OpenViking HTTP connection settings:

```python
from langchain_openviking import OpenVikingStore

store = OpenVikingStore(
    url=OPENVIKING_URL,
    api_key=OPENVIKING_API_KEY,
    root_uri="viking://~/memories/langgraph_store",
)
```

The package default `root_uri` is `viking://user/memories/langgraph_store`. Newer OpenViking servers reject that uid-less form, so pass the `viking://~` home alias (as above) or an explicit `viking://user/<uid>/...` URI.

## Usage

Use `put` to write a JSON-serializable mapping under a namespace and key:

```python
store.put(
    ("users", "ada"),
    "preferences",
    {"color": "azure"},
)
```

Use `get` to retrieve the stored item:

```python
item = store.get(("users", "ada"), "preferences")
print(item.value)
```

Use `search` with a namespace prefix. Pass `query` for semantic search:

```python
results = store.search(("users",), query="azure", limit=3)
```

Use `delete` to remove a key:

```python
store.delete(("users", "ada"), "preferences")
```

## API reference

For detailed documentation, see the [OpenViking LangChain and LangGraph integration guide](https://github.com/volcengine/OpenViking/blob/main/docs/en/agent-integrations/07-langchain-langgraph.md#langgraph-store) and the [`OpenVikingStore` source for v0.1.0](https://github.com/volcengine/OpenViking/blob/langchain-openviking@0.1.0/integrations/langchain/src/langchain_openviking/store.py).

See also the [LangGraph store integrations](../long-term-memory.md) list.

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/stores/openviking.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
