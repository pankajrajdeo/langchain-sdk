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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/mcp/elicitation.py#L72)
