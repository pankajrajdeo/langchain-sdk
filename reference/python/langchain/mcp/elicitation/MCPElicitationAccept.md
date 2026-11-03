---
title: "MCPElicitationAccept"
description: "An answer to an MCPElicitationRequest."
source: "https://reference.langchain.com/python/langchain/mcp/elicitation/MCPElicitationAccept"
category: "reference"
tags: [reference, langchain, mcp, elicitation, mcpelicitationaccept]
---

# MCPElicitationAccept

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/elicitation/MCPElicitationAccept)

An answer to an `MCPElicitationRequest`.

## Signature

```python
MCPElicitationAccept()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    action: Literal['accept'],
    content: NotRequired[MCPFormContent | None],
)
```

| Name | Type |
|------|------|
| `action` | `Literal['accept']` |
| `content` | `NotRequired[MCPFormContent \| None]` |

## Properties

- `action`
- `content`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/mcp/elicitation.py#L108)
