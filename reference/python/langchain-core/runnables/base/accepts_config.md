---
title: "accepts_config"
description: "Check if a callable accepts a config argument."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/accepts_config"
category: "reference"
tags: [reference, langchain-core, runnables, base, accepts_config]
---

# accepts_config

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/accepts_config)

Check if a callable accepts a config argument.

## Signature

```python
accepts_config(
    callable: Callable[..., Any],
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `callable` | `Callable[..., Any]` | Yes | The callable to check. |

## Returns

`bool`

`True` if the callable accepts a config argument, `False` otherwise.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/runnables/utils.py#L101)
