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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L107)
