---
title: "SubAgent"
description: "Specification for a declarative subagent."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagent]
---

# SubAgent

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent)

Specification for a declarative subagent.

By default the subagent is isolated: it receives only the delegated task
description. Setting `mode="fork"` makes it continue the parent's
conversation instead.

!!! warning "Experimental"

    `mode="fork"` is experimental and may change in a future release.

When using `create_deep_agent`, subagents automatically receive
a default middleware stack before any custom `middleware` specified in
this spec.

`name` and `description` are required; all other fields are optional.
See the individual attributes for configuration details.

## Signature

```python
SubAgent()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    name: str,
    description: str,
    tools: NotRequired[Sequence[BaseTool | Callable | dict[str, Any]]],
    model: NotRequired[str | BaseChatModel],
    middleware: NotRequired[list[AgentMiddleware]],
    interrupt_on: NotRequired[dict[str, bool | InterruptOnConfig]],
    skills: NotRequired[list[str]],
    permissions: NotRequired[list[FilesystemPermission]],
    response_format: NotRequired[ResponseFormat[Any] | type | dict[str, Any]],
    system_prompt: NotRequired[str],
    mode: NotRequired[Literal['isolated', 'fork']],
)
```

| Name | Type |
|------|------|
| `name` | `str` |
| `description` | `str` |
| `tools` | `NotRequired[Sequence[BaseTool \| Callable \| dict[str, Any]]]` |
| `model` | `NotRequired[str \| BaseChatModel]` |
| `middleware` | `NotRequired[list[AgentMiddleware]]` |
| `interrupt_on` | `NotRequired[dict[str, bool \| InterruptOnConfig]]` |
| `skills` | `NotRequired[list[str]]` |
| `permissions` | `NotRequired[list[FilesystemPermission]]` |
| `response_format` | `NotRequired[ResponseFormat[Any] \| type \| dict[str, Any]]` |
| `system_prompt` | `NotRequired[str]` |
| `mode` | `NotRequired[Literal['isolated', 'fork']]` |

## Properties

- `name`
- `description`
- `tools`
- `model`
- `middleware`
- `interrupt_on`
- `skills`
- `permissions`
- `response_format`
- `system_prompt`
- `mode`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/subagents.py#L84)
