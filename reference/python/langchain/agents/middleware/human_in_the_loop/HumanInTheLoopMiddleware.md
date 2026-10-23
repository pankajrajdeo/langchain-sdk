---
title: "HumanInTheLoopMiddleware"
description: "Pause the agent so a person can review tool calls before they run."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, humanintheloopmiddleware]
---

# HumanInTheLoopMiddleware

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware)

Pause the agent so a person can review tool calls before they run.

Each tool in `interrupt_on` needs a decision before it runs: approve, edit, reject,
or respond. The pause is a LangGraph `interrupt`, so the agent needs a checkpointer,
and the run continues with `Command(resume=...)`.

`interrupt_mode` sets how the agent pauses:

- `"batched"` (default): one interrupt per model turn. Its value is a `HITLRequest`
    listing every gated call, answered with a `HITLResponse` whose decisions match
    the calls by position.
- `"per_call"`: one interrupt per gated tool call, as the call starts. Its value is
    a `ToolApprovalRequest` and its `response_schema` lists the decisions that tool
    allows. Each is answered with a single `Decision` keyed by interrupt ID, and
    LangGraph checks the answer against the schema before saving it. `"per_call"`
    is planned to become the default in the next major release.

## Signature

```python
HumanInTheLoopMiddleware(
    self,
    interrupt_on: dict[str, bool | InterruptOnConfig],
    *,
    description_prefix: str = 'Tool execution requires approval',
    edit_notice: str | None = _EDIT_NOTICE,
    interrupt_mode: InterruptMode = 'batched',
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `interrupt_on` | `dict[str, bool \| InterruptOnConfig]` | Yes | Mapping of tool name to allowed actions.  If a tool doesn't have an entry, it's auto-approved by default.  * `True` indicates all decisions are allowed: approve, edit, reject,     and respond. * `False` indicates that the tool is auto-approved. * `InterruptOnConfig` indicates the specific decisions allowed for this     tool.      The `InterruptOnConfig` can include a `description` field (`str` or     `Callable`) for custom formatting of the interrupt description.      A `when` predicate can also be provided to dynamically control     whether a tool call triggers an interrupt. |
| `description_prefix` | `str` | No | The prefix to use when constructing action requests.  This is used to provide context about the tool call and the action being requested.  Not used if a tool has a `description` in its `InterruptOnConfig`. (default: `'Tool execution requires approval'`) |
| `edit_notice` | `str \| None` | No | Text prepended to the result of a tool call a reviewer replaced via an `edit` decision. Pass `None` to add nothing. (default: `_EDIT_NOTICE`) |
| `interrupt_mode` | `InterruptMode` | No | How the agent pauses for review.  - `"batched"` (default): one interrupt per model turn for all gated     tool calls, answered with a `HITLResponse`. - `"per_call"`: one `ToolApprovalRequest` interrupt per gated tool     call, with a typed `response_schema`, answered with a single     `Decision` keyed by interrupt ID.  In `per_call` mode, LangGraph checks each answer before saving it:  - An edit can't switch tools, and its args must match the tool's     argument types. Args the tool doesn't declare are ignored, as     they are when the model sends them.     Validator methods on the tool's `args_schema` run when the tool     does. For a tool whose arguments are a JSON schema rather than a     Pydantic model, edits are shown in `response_schema` but not     checked. - An invalid answer raises `pydantic.ValidationError` and isn't     saved, so the same interrupt can be answered again.  !!! warning "Answering several calls at once"      If one of several answers sent together is invalid, the others'     tools may already have run even if they still show as pending,     and answering them again would run them twice. Check answers     against `response_schema` before sending them together, or send     one at a time.  !!! warning "Middleware order in `per_call` mode"      The review happens as the tool call starts, inside the tool-call     middleware chain. List this middleware before tool retry or     error-handling middleware so it wraps them, and don't enable it     on subclasses that raise their own interrupts in `after_model`.     On resume, each paused tool call runs the middleware listed     before this one again up to the pause, so that middleware must     not have side effects before calling `handler`. The tool itself     runs only after the answer.  As in `batched` mode, running the agent asynchronously (`ainvoke`, `astream`) needs Python 3.11 or later. (default: `'batched'`) |

## Extends

- `AgentMiddleware[StateT, ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    interrupt_on: dict[str, bool | InterruptOnConfig],
    *,
    description_prefix: str = 'Tool execution requires approval',
    edit_notice: str | None = _EDIT_NOTICE,
    interrupt_mode: InterruptMode = 'batched',
) -> None
```

| Name | Type |
|------|------|
| `interrupt_on` | `dict[str, bool \| InterruptOnConfig]` |
| `description_prefix` | `str` |
| `edit_notice` | `str \| None` |
| `interrupt_mode` | `InterruptMode` |

## Properties

- `state_schema`
- `interrupt_mode`
- `edit_notice`
- `interrupt_on`
- `description_prefix`

## Methods

- [`after_model()`](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/after_model)
- [`aafter_model()`](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/aafter_model)
- [`wrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/wrap_tool_call)
- [`awrap_tool_call()`](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HumanInTheLoopMiddleware/awrap_tool_call)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/fbb8a35da7023ac0382c3b22f047337861bd3486/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L396)
