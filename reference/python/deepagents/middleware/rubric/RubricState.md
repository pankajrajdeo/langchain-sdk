---
title: "RubricState"
description: "State schema for RubricMiddleware."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/RubricState"
category: "reference"
tags: [reference, deepagents, middleware, rubric, rubricstate]
---

# RubricState

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/RubricState)

State schema for `RubricMiddleware`.

Only `rubric` is part of the public I/O schema -- callers write a
rubric and read the improved agent response back from `messages`.

Everything else is bookkeeping: status, iteration count, accumulated
evaluations, and rubric-attempt tracking are annotated with
[`PrivateStateAttr`][langchain.agents.middleware.types.PrivateStateAttr]
so they are omitted from input/output schemas. Tests, evals, and
observability consumers can still reach them via the `on_evaluation`
callback, the `rubric_evaluation_*` stream events, or
`agent.get_state(config).values` on a checkpointed thread.

## Signature

```python
RubricState()
```

## Extends

- `AgentState`

## Properties

- `rubric`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/rubric.py#L260)
