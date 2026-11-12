---
title: "AutoModeMiddleware"
description: "Allow low-risk tool calls and block risky calls using a decision model."
source: "https://reference.langchain.com/python/langchain/agents/middleware/auto_mode/AutoModeMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, auto_mode, automodemiddleware]
---

# AutoModeMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/auto_mode/AutoModeMiddleware)

Allow low-risk tool calls and block risky calls using a decision model.

The middleware intercepts explicitly configured tools immediately before execution
and asks a `Noul` question for the probability that each call is risky or
insufficiently authorized. Calls below 0.5 execute normally. Calls at or above it
return an error `ToolMessage` without invoking the tool handler. Tool names not
listed in `tools` bypass classification.

The classifier receives the proposed tool call, the tool description, and up to 30
recent messages. Classification failures propagate and the tool handler is not
called. This middleware blocks calls; it does not request human approval.

!!! warning "Beta"

    This middleware is in beta. Its API may change without notice.

## Signature

```python
AutoModeMiddleware(
    self,
    *,
    tools: Sequence[str | BaseTool],
    instructions: str = _DEFAULT_INSTRUCTIONS,
    criteria: NoulCriteria | None = None,
    classifier: BaseDecisionModel,
)
```

## Description

??? example "Customize the criteria"

```python
from langchain.agents import create_agent
from langchain.agents.middleware import AutoModeMiddleware
from langchain_core.decisions import NoulCriteria

auto_mode = AutoModeMiddleware(
    tools=[delete_file],
    criteria=NoulCriteria(
        true="The call writes, deletes, publishes, or changes access.",
        false="The call only reads public or user-provided data.",
    ),
    classifier=classifier,
)
agent = create_agent(
    model,
    tools=[read_file, delete_file],
    middleware=[auto_mode],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `tools` | `Sequence[str \| BaseTool]` | Yes | Tool names or `BaseTool` instances to classify before execution. Unlisted tools are passed to the handler without classification. |
| `instructions` | `str` | No | Classification instructions sent to the decision model. (default: `_DEFAULT_INSTRUCTIONS`) |
| `criteria` | `NoulCriteria \| None` | No | Optional descriptions of the blocked and allowed outcomes. (default: `None`) |
| `classifier` | `BaseDecisionModel` | Yes | Decision model used to classify tool calls. |

## Extends

- `AgentMiddleware[AgentState[ResponseT], ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    tools: Sequence[str | BaseTool],
    instructions: str = _DEFAULT_INSTRUCTIONS,
    criteria: NoulCriteria | None = None,
    classifier: BaseDecisionModel,
) -> None
```

| Name | Type |
|------|------|
| `tools` | `Sequence[str \| BaseTool]` |
| `instructions` | `str` |
| `criteria` | `NoulCriteria \| None` |
| `classifier` | `BaseDecisionModel` |

## Properties

- `trace_policy`
- `config`
- `classifier`

## Methods

- [`wrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/auto_mode/AutoModeMiddleware/wrap_tool_call)
- [`awrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/auto_mode/AutoModeMiddleware/awrap_tool_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/auto_mode.py#L64)
