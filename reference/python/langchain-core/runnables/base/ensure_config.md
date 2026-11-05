---
title: "ensure_config"
description: "Ensure that a config is a dict with all keys present."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/ensure_config"
category: "reference"
tags: [reference, langchain-core, runnables, base, ensure_config]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/runnables/config.py#L255)
