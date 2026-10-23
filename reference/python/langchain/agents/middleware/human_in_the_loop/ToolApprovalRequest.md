---
title: "ToolApprovalRequest"
description: "Interrupt value raised once per gated tool call in per_call mode."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/ToolApprovalRequest"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, toolapprovalrequest]
---

# ToolApprovalRequest

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/ToolApprovalRequest)

Interrupt value raised once per gated tool call in `per_call` mode.

Takes the place of `HITLRequest`. Answer it with a single `Decision`, keyed by the
interrupt's ID, not a `HITLResponse`. The interrupt's `response_schema` lists the
decisions allowed for the tool and, for edits, the tool's argument schema.

## Signature

```python
ToolApprovalRequest()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['tool_approval'],
    tool_call_id: str,
    name: str,
    args: dict[str, Any],
    description: str,
)
```

| Name | Type |
|------|------|
| `type` | `Literal['tool_approval']` |
| `tool_call_id` | `str` |
| `name` | `str` |
| `args` | `dict[str, Any]` |
| `description` | `str` |

## Properties

- `type`
- `tool_call_id`
- `name`
- `args`
- `description`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/fbb8a35da7023ac0382c3b22f047337861bd3486/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L172)
