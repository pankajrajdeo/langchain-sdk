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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d1d95b79213b0212613ae1aa4fad38bea6f1dccf/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L106)
