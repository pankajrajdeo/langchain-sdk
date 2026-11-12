---
title: "ModelChoice"
description: "A model available to the router and the criterion for selecting it."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelChoice"
category: "reference"
tags: [reference, langchain, agents, middleware, model_router, modelchoice]
---

# ModelChoice

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelChoice)

A model available to the router and the criterion for selecting it.

## Signature

```python
ModelChoice(
    self,
    model: str | BaseChatModel,
    criteria: JsonValue,
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `str \| BaseChatModel` | Yes | LangChain model instance or model string accepted by `init_chat_model`. |
| `criteria` | `JsonValue` | Yes | Description of the tasks suited to the model. |

## Constructors

```python
__init__(
    self,
    model: str | BaseChatModel,
    criteria: JsonValue,
) -> None
```

| Name | Type |
|------|------|
| `model` | `str \| BaseChatModel` |
| `criteria` | `JsonValue` |

## Properties

- `model`
- `criteria`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/model_router.py#L35)
