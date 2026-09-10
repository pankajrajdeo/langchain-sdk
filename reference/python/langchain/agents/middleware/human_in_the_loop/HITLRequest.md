---
title: "HITLRequest"
description: "Request for human feedback on a sequence of actions requested by a model."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HITLRequest"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, hitlrequest]
---

# HITLRequest

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/HITLRequest)

Request for human feedback on a sequence of actions requested by a model.

## Signature

```python
HITLRequest()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    action_requests: list[ActionRequest],
    review_configs: list[ReviewConfig],
)
```

| Name | Type |
|------|------|
| `action_requests` | `list[ActionRequest]` |
| `review_configs` | `list[ReviewConfig]` |

## Properties

- `action_requests`
- `review_configs`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L67)
