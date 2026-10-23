---
title: "AsyncSubAgentMiddleware"
description: "Middleware for async subagents running on remote Agent Protocol servers."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagentmiddleware]
---

# AsyncSubAgentMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware)

Middleware for async subagents running on remote Agent Protocol servers.

This middleware adds tools for launching, monitoring, and updating
background tasks on remote Agent Protocol servers. Unlike the synchronous
`SubAgentMiddleware`, async subagents return immediately with a task ID,
allowing the main agent to continue working while subagents execute.

Works with any Agent Protocol-compliant server — LangGraph Platform
(managed) or self-hosted (e.g. a FastAPI server implementing the Agent
Protocol spec).

Task IDs are persisted in the agent state under `async_tasks` so they
survive context compaction/offloading and can be accessed programmatically.

!!! warning "Beta"

    On an Agent Server, the agent is told when its async subagent tasks
    finish, fail or wait for the user: before each model call and after
    its final answer while it runs, and through a new run when a deep
    agent subagent on this deployment ends while it's idle. This needs the async path (`ainvoke`,
    which the Agent Server uses); with `invoke`, only the tools work. This
    may change.

## Signature

```python
AsyncSubAgentMiddleware(
    self,
    *,
    async_subagents: list[AsyncSubAgent],
    system_prompt: str | None = None,
)
```

## Description

**Example:**

```python
from deepagents.middleware.async_subagents import AsyncSubAgentMiddleware

middleware = AsyncSubAgentMiddleware(
    async_subagents=[
        {
            "name": "researcher",
            "description": "Research agent for deep analysis",
            "url": "https://my-deployment.langsmith.dev",
            "graph_id": "research_agent",
        }
    ],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `async_subagents` | `list[AsyncSubAgent]` | Yes | List of async subagent specifications.  Each must include `name`, `description`, and `graph_id`. `url` is optional — omit it to use ASGI transport for local servers. |
| `system_prompt` | `str \| None` | No | Instructions appended to the main agent's system prompt about how to use the async subagent tools. (default: `None`) |

## Extends

- `AgentMiddleware[Any, ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    async_subagents: list[AsyncSubAgent],
    system_prompt: str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `async_subagents` | `list[AsyncSubAgent]` |
| `system_prompt` | `str \| None` |

## Properties

- `trace_policy`
- `state_schema`
- `tools`
- `system_prompt`

## Methods

- [`before_agent()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/before_agent)
- [`abefore_agent()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/abefore_agent)
- [`before_model()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/before_model)
- [`abefore_model()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/abefore_model)
- [`after_model()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/after_model)
- [`aafter_model()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/aafter_model)
- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgentMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/async_subagents.py#L1508)
