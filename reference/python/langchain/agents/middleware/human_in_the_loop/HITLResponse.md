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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L289)
