---
title: "set_llm_cache"
description: "Set a new LLM cache, overwriting the previous value, if any."
source: "https://reference.langchain.com/python/langchain-core/globals/set_llm_cache"
category: "reference"
tags: [reference, langchain-core, globals, set_llm_cache]
---

# set_llm_cache

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/globals/set_llm_cache)

Set a new LLM cache, overwriting the previous value, if any.

## Signature

```python
set_llm_cache(
    value: Optional[BaseCache],
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `value` | `Optional[BaseCache]` | Yes | The new LLM cache to use. If `None`, the LLM cache is disabled. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/globals.py#L56)
