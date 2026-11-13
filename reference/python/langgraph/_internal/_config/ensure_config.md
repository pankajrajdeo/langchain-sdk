---
title: "ensure_config"
description: "Return a config with all keys, merging any provided configs."
source: "https://reference.langchain.com/python/langgraph/_internal/_config/ensure_config"
category: "reference"
tags: [reference, langgraph, internal, config, ensure_config]
---

# ensure_config

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_config/ensure_config)

Return a config with all keys, merging any provided configs.

## Signature

```python
ensure_config(
    configs: RunnableConfig | None = (),
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*configs` | `RunnableConfig \| None` | No | Configs to merge before ensuring defaults. (default: `()`) |

## Returns

`RunnableConfig`

The merged and ensured config.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/_internal/_config.py#L334)
