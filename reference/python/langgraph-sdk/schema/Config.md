---
title: "Config"
description: "Configuration options for a call."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/Config"
category: "reference"
tags: [reference, langgraph-sdk, schema, config]
---

# Config

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/Config)

Configuration options for a call.

## Signature

```python
Config()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    tags: list[str],
    recursion_limit: int,
    configurable: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `tags` | `list[str]` |
| `recursion_limit` | `int` |
| `configurable` | `dict[str, Any]` |

## Properties

- `tags`
- `recursion_limit`
- `configurable`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/schema.py#L185)
