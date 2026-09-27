---
title: "accepts_run_manager"
description: "Check if a callable accepts a run_manager argument."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/accepts_run_manager"
category: "reference"
tags: [reference, langchain-core, runnables, base, accepts_run_manager]
---

# accepts_run_manager

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/accepts_run_manager)

Check if a callable accepts a run_manager argument.

## Signature

```python
accepts_run_manager(
    callable: Callable[..., Any],
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `callable` | `Callable[..., Any]` | Yes | The callable to check. |

## Returns

`bool`

`True` if the callable accepts a run_manager argument, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/utils.py#L85)
