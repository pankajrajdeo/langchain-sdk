---
title: "cache_read"
description: "Input tokens that were cached and there was a cache hit."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/InputTokenDetails/cache_read"
category: "reference"
tags: [reference, langchain-core, messages, ai, inputtokendetails, cache_read]
---

# cache_read

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/InputTokenDetails/cache_read)

Input tokens that were cached and there was a cache hit.

Since there was a cache hit, the tokens were read from the cache. More precisely,
the model state given these tokens was read from the cache.

## Signature

```python
cache_read: int
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/messages/ai.py#L66)
