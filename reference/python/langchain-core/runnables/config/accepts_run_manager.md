---
title: "accepts_run_manager"
description: "Check if a callable accepts a run_manager argument."
source: "https://reference.langchain.com/python/langchain-core/runnables/config/accepts_run_manager"
category: "reference"
tags: [reference, langchain-core, runnables, config, accepts_run_manager]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/runnables/utils.py#L85)
