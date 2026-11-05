---
title: "AssistantBase"
description: "Base model for an assistant."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/AssistantBase"
category: "reference"
tags: [reference, langgraph-sdk, schema, assistantbase]
---

# AssistantBase

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/AssistantBase)

Base model for an assistant.

## Signature

```python
AssistantBase()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    assistant_id: str,
    graph_id: str,
    config: Config,
    context: Context,
    created_at: datetime,
    metadata: Json,
    version: int,
    name: str,
    description: str | None,
)
```

| Name | Type |
|------|------|
| `assistant_id` | `str` |
| `graph_id` | `str` |
| `config` | `Config` |
| `context` | `Context` |
| `created_at` | `datetime` |
| `metadata` | `Json` |
| `version` | `int` |
| `name` | `str` |
| `description` | `str \| None` |

## Properties

- `assistant_id`
- `graph_id`
- `config`
- `context`
- `created_at`
- `metadata`
- `version`
- `name`
- `description`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/sdk-py/langgraph_sdk/schema.py#L246)
