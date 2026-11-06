---
title: "LangGraphClient"
description: "Top-level client for LangGraph API."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/client/LangGraphClient"
category: "reference"
tags: [reference, langgraph-sdk, async, client, langgraphclient]
---

# LangGraphClient

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/client/LangGraphClient)

Top-level client for LangGraph API.

## Signature

```python
LangGraphClient(
    self,
    client: httpx.AsyncClient,
)
```

## Constructors

```python
__init__(
    self,
    client: httpx.AsyncClient,
) -> None
```

| Name | Type |
|------|------|
| `client` | `httpx.AsyncClient` |

## Properties

- `http`
- `assistants`
- `threads`
- `runs`
- `crons`
- `store`

## Methods

- [`aclose()`](https://reference.langchain.com/python/langgraph-sdk/_async/client/LangGraphClient/aclose)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5847733bcb186c26b32da5cc822eaf8a89deffeb/libs/sdk-py/langgraph_sdk/_async/client.py#L143)
