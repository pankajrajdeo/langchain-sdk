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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/runnables/utils.py#L116)
