---
title: "ensure_config"
description: "Ensure that a config is a dict with all keys present."
source: "https://reference.langchain.com/python/langchain-core/language_models/chat_models/ensure_config"
category: "reference"
tags: [reference, langchain-core, language_models, chat_models, ensure_config]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/runnables/config.py#L255)
