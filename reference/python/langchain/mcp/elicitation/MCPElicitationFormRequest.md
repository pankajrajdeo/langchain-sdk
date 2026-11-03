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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/mcp/elicitation.py#L56)
