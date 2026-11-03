---
title: "HITLResponse"
description: "Response payload for a HITLRequest."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HITLResponse"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, hitlresponse]
---

# HITLResponse

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HITLResponse)

Response payload for a HITLRequest.

## Signature

```python
HITLResponse()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    decisions: list[Decision],
)
```

| Name | Type |
|------|------|
| `decisions` | `list[Decision]` |

## Properties

- `decisions`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L288)
