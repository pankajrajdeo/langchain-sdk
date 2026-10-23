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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/fbb8a35da7023ac0382c3b22f047337861bd3486/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L287)
