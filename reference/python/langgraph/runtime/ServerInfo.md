---
title: "ServerInfo"
description: "Metadata injected by LangGraph Server. None when running open-source LangGraph without LangSmith deployments."
source: "https://reference.langchain.com/python/langgraph/runtime/ServerInfo"
category: "reference"
tags: [reference, langgraph, runtime, serverinfo]
---

# ServerInfo

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/runtime/ServerInfo)

Metadata injected by LangGraph Server. None when running open-source LangGraph without LangSmith deployments.

## Signature

```python
ServerInfo(
    self,
    assistant_id: str,
    graph_id: str,
    user: BaseUser | None = None,
)
```

## Constructors

```python
__init__(
    self,
    assistant_id: str,
    graph_id: str,
    user: BaseUser | None = None,
) -> None
```

| Name | Type |
|------|------|
| `assistant_id` | `str` |
| `graph_id` | `str` |
| `user` | `BaseUser \| None` |

## Properties

- `assistant_id`
- `graph_id`
- `user`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/runtime.py#L60)
