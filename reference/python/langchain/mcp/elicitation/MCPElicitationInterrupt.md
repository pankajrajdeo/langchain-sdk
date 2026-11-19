---
title: "MCPElicitationInterrupt"
description: "Interrupt payload raised while an MCP tool call waits on input."
source: "https://reference.langchain.com/python/langchain/mcp/elicitation/MCPElicitationInterrupt"
category: "reference"
tags: [reference, langchain, mcp, elicitation, mcpelicitationinterrupt]
---

# MCPElicitationInterrupt

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/elicitation/MCPElicitationInterrupt)

Interrupt payload raised while an MCP tool call waits on input.

## Signature

```python
MCPElicitationInterrupt()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    type: Literal['mcp_elicitation'],
    tool_name: str,
    requests: list[MCPElicitationRequest],
)
```

| Name | Type |
|------|------|
| `type` | `Literal['mcp_elicitation']` |
| `tool_name` | `str` |
| `requests` | `list[MCPElicitationRequest]` |

## Properties

- `type`
- `tool_name`
- `requests`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/mcp/elicitation.py#L93)
