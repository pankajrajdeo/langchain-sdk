---
title: "InterruptMode"
description: "How HITL pauses: one interrupt per model turn (batched) or per gated tool call."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptMode"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, interruptmode]
---

# InterruptMode

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/InterruptMode)

How HITL pauses: one interrupt per model turn (`batched`) or per gated tool call.

## Signature

```python
InterruptMode = Literal['batched', 'per_call']
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L170)
