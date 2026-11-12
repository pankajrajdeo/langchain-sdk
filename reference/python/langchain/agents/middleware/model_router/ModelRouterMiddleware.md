---
title: "ModelRouterMiddleware"
description: "Select an agent's model with a decision model's Choice answer."
source: "https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, model_router, modelroutermiddleware]
---

# ModelRouterMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware)

Select an agent's model with a decision model's `Choice` answer.

The middleware classifies the latest human message once before an agent run,
stores the complete `ChoiceAnswer` in agent state, and uses its selected label for
every model call in the run. Keeping the complete answer makes probabilities and
confidence available in state and traces. Classifier failures propagate and
terminate the run rather than silently selecting a different model.

!!! warning "Beta"

    This middleware is in beta. Its API may change without notice.

## Signature

```python
ModelRouterMiddleware(
    self,
    *,
    choices: Mapping[str, ModelChoice],
    instructions: Content,
    classifier: BaseDecisionModel,
)
```

## Description

??? example "Route agent calls by task"

```python
from langchain.agents import create_agent
from langchain.agents.middleware import ModelChoice, ModelRouterMiddleware

router = ModelRouterMiddleware(
    choices={
        "fast": ModelChoice(
            model="openai:gpt-5-mini",
            criteria="Simple, well-scoped tasks.",
        ),
        "powerful": ModelChoice(
            model=powerful_model,
            criteria="Complex tasks requiring deeper reasoning.",
        ),
    },
    instructions="Choose the least costly model suited to the task.",
    classifier=classifier,
)
agent = create_agent("openai:gpt-5-mini", middleware=[router])
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `choices` | `Mapping[str, ModelChoice]` | Yes | Named model choices, each containing a LangChain model or model string and the criterion for selecting it. |
| `instructions` | `Content` | Yes | Instructions the classifier should follow when selecting a route. |
| `classifier` | `BaseDecisionModel` | Yes | Decision model used to select a route. |

## Extends

- `AgentMiddleware[_ModelRouterState]`

## Constructors

```python
__init__(
    self,
    *,
    choices: Mapping[str, ModelChoice],
    instructions: Content,
    classifier: BaseDecisionModel,
) -> None
```

| Name | Type |
|------|------|
| `choices` | `Mapping[str, ModelChoice]` |
| `instructions` | `Content` |
| `classifier` | `BaseDecisionModel` |

## Properties

- `state_schema`
- `trace_policy`
- `config`
- `models`
- `classifier`

## Methods

- [`before_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/before_agent)
- [`abefore_agent()`](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/abefore_agent)
- [`wrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/langchain/agents/middleware/model_router/ModelRouterMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/model_router.py#L71)
