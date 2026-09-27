---
title: "TasksStreamPart"
description: "Stream part emitted for stream_mode=\"tasks\"."
source: "https://reference.langchain.com/python/langgraph-sdk/schema/TasksStreamPart"
category: "reference"
tags: [reference, langgraph-sdk, schema, tasksstreampart]
---

# TasksStreamPart

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/schema/TasksStreamPart)

Stream part emitted for `stream_mode="tasks"`.

## Signature

```python
TasksStreamPart()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['tasks'],
    ns: list[str],
    data: TaskPayload | TaskResultPayload,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['tasks']` |
| `ns` | `list[str]` |
| `data` | `TaskPayload \| TaskResultPayload` |

## Properties

- `type`
- `ns`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/sdk-py/langgraph_sdk/schema.py#L825)
