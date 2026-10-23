---
title: "AsyncSubAgent"
description: "Specification for an async subagent running on a remote Agent Protocol server."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, asyncsubagent]
---

# AsyncSubAgent

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/AsyncSubAgent)

Specification for an async subagent running on a remote [Agent Protocol](https://github.com/langchain-ai/agent-protocol) server.

Async subagents connect to any Agent Protocol-compliant server via the
LangGraph SDK. They run as background tasks that the main agent can
monitor and update.

Compatible with LangGraph Platform / LangSmith Deployment (managed) and
self-hosted servers.

Authentication for LangGraph Platform / LangSmith Deployment is handled
automatically by the SDK via environment variables (`LANGGRAPH_API_KEY`,
`LANGSMITH_API_KEY`, or `LANGCHAIN_API_KEY`). For self-hosted servers,
pass custom auth via `headers`.

!!! note "Async invocation required for local ASGI transport"

    Omitting `url` uses in-process ASGI transport for a local server. This
    transport is available only through an async parent-agent entrypoint,
    such as `ainvoke`. The synchronous `invoke` path requires a URL for a
    reachable Agent Protocol server.

!!! warning "Beta"

    When tracing is on, launches and updates of subagents on this deployment
    (no `url`) send the parent's LangSmith trace headers, so a receiver can
    nest the subagent's run under the parent's trace. This may change.

    Each task's thread is created with
    `metadata={"subagent_name": ..., "parent_thread_id": ...}`, so apps can
    find a parent's subagent threads with `threads.search`, and a subagent's
    graph factory can read them from its run's `config["metadata"]`.
    `subagent_name` is this spec's `name`. This may change.

    Launches and updates on this deployment run with the parent's current run
    context, not the child's prior context. Queued updates capture that context
    when sent, not when they start. A remote subagent (`url`) receives no context.

## Signature

```python
AsyncSubAgent()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    description: str,
    graph_id: str,
    url: NotRequired[str],
    headers: NotRequired[dict[str, str]],
    webhook: NotRequired[str],
    update_strategy: NotRequired[Literal['interrupt', 'enqueue']],
    notify_parent: NotRequired[bool],
    mode: NotRequired[Literal['isolated', 'fork']],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `description` | `str` |
| `graph_id` | `str` |
| `url` | `NotRequired[str]` |
| `headers` | `NotRequired[dict[str, str]]` |
| `webhook` | `NotRequired[str]` |
| `update_strategy` | `NotRequired[Literal['interrupt', 'enqueue']]` |
| `notify_parent` | `NotRequired[bool]` |
| `mode` | `NotRequired[Literal['isolated', 'fork']]` |

## Properties

- `name`
- `description`
- `graph_id`
- `url`
- `headers`
- `webhook`
- `update_strategy`
- `notify_parent`
- `mode`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/async_subagents.py#L56)
