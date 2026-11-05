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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/schema.py#L185)
