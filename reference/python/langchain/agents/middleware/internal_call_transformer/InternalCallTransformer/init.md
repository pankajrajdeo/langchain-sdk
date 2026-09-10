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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/internal_call_transformer.py#L68)
