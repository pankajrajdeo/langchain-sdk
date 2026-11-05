---
title: "init"
description: "Return an empty projection — this transformer only suppresses events."
source: "https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/InternalCallTransformer/init"
category: "reference"
tags: [reference, langchain, agents, middleware, internal_call_transformer, internalcalltransformer, init]
---

# init

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/InternalCallTransformer/init)

Return an empty projection — this transformer only suppresses events.

## Signature

```python
init(
    self,
) -> dict[str, Any]
```

## Returns

`dict[str, Any]`

An empty mapping; no `run.<key>` projection is added.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d1d95b79213b0212613ae1aa4fad38bea6f1dccf/libs/langchain_v1/langchain/agents/middleware/internal_call_transformer.py#L68)
