---
title: "HumanInTheLoopMiddleware"
description: "Human in the loop middleware."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, humanintheloopmiddleware]
---

# HumanInTheLoopMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware)

Human in the loop middleware.

## Signature

```python
HumanInTheLoopMiddleware(
    self,
    interrupt_on: dict[str, bool | InterruptOnConfig],
    *,
    description_prefix: str = 'Tool execution requires approval',
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `interrupt_on` | `dict[str, bool \| InterruptOnConfig]` | Yes | Mapping of tool name to allowed actions.  If a tool doesn't have an entry, it's auto-approved by default.  * `True` indicates all decisions are allowed: approve, edit, reject,     and respond. * `False` indicates that the tool is auto-approved. * `InterruptOnConfig` indicates the specific decisions allowed for this     tool.      The `InterruptOnConfig` can include a `description` field (`str` or     `Callable`) for custom formatting of the interrupt description.      A `when` predicate can also be provided to dynamically control     whether a tool call triggers an interrupt. |
| `description_prefix` | `str` | No | The prefix to use when constructing action requests.  This is used to provide context about the tool call and the action being requested.  Not used if a tool has a `description` in its `InterruptOnConfig`. (default: `'Tool execution requires approval'`) |

## Extends

- `AgentMiddleware[StateT, ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    interrupt_on: dict[str, bool | InterruptOnConfig],
    *,
    description_prefix: str = 'Tool execution requires approval',
) -> None
```

| Name | Type |
|------|------|
| `interrupt_on` | `dict[str, bool \| InterruptOnConfig]` |
| `description_prefix` | `str` |

## Properties

- `interrupt_on`
- `description_prefix`

## Methods

- [`after_model()`](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/after_model)
- [`aafter_model()`](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/aafter_model)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L217)
