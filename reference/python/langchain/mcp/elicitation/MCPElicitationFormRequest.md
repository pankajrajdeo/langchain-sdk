---
title: "MCPElicitationFormRequest"
description: "A request for data matching a schema."
source: "https://reference.langchain.com/python/langchain/mcp/elicitation/MCPElicitationFormRequest"
category: "reference"
tags: [reference, langchain, mcp, elicitation, mcpelicitationformrequest]
---

# MCPElicitationFormRequest

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/elicitation/MCPElicitationFormRequest)

A request for data matching a schema.

## Signature

```python
MCPElicitationFormRequest()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    key: str,
    message: str,
    mode: Literal['form'],
    requested_schema: dict[str, Any],
)
```

| Name | Type |
|------|------|
| `key` | `str` |
| `message` | `str` |
| `mode` | `Literal['form']` |
| `requested_schema` | `dict[str, Any]` |

## Properties

- `key`
- `message`
- `mode`
- `requested_schema`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/fbb8a35da7023ac0382c3b22f047337861bd3486/libs/langchain_v1/langchain/mcp/elicitation.py#L56)
