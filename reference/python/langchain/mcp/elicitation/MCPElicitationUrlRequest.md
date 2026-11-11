---
title: "MCPElicitationUrlRequest"
description: "A request for the human to visit an address."
source: "https://reference.langchain.com/python/langchain/mcp/elicitation/MCPElicitationUrlRequest"
category: "reference"
tags: [reference, langchain, mcp, elicitation, mcpelicitationurlrequest]
---

# MCPElicitationUrlRequest

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/mcp/elicitation/MCPElicitationUrlRequest)

A request for the human to visit an address.

## Signature

```python
MCPElicitationUrlRequest()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    key: str,
    message: str,
    mode: Literal['url'],
    url: str,
)
```

| Name | Type |
|------|------|
| `key` | `str` |
| `message` | `str` |
| `mode` | `Literal['url']` |
| `url` | `str` |

## Properties

- `key`
- `message`
- `mode`
- `url`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/mcp/elicitation.py#L73)
