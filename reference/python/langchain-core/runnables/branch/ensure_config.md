---
title: "ensure_config"
description: "Ensure that a config is a dict with all keys present."
source: "https://reference.langchain.com/python/langchain-core/runnables/branch/ensure_config"
category: "reference"
tags: [reference, langchain-core, runnables, branch, ensure_config]
---

# ensure_config

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/ensure_config)

Ensure that a config is a dict with all keys present.

## Signature

```python
ensure_config(
    config: RunnableConfig | None = None,
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The config to ensure. (default: `None`) |

## Returns

`RunnableConfig`

The ensured config.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/config.py#L255)
