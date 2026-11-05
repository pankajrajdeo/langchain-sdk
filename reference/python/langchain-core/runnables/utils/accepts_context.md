---
title: "accepts_context"
description: "Check if a callable accepts a context argument."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/accepts_context"
category: "reference"
tags: [reference, langchain-core, runnables, utils, accepts_context]
---

# accepts_context

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/accepts_context)

Check if a callable accepts a context argument.

## Signature

```python
accepts_context(
    callable: Callable[..., Any],
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `callable` | `Callable[..., Any]` | Yes | The callable to check. |

## Returns

`bool`

`True` if the callable accepts a context argument, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/runnables/utils.py#L116)
