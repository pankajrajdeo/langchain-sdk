---
title: "ensure_config"
description: "Return a config with all keys, merging any provided configs."
source: "https://reference.langchain.com/python/langgraph/pregel/main/ensure_config"
category: "reference"
tags: [reference, langgraph, pregel, main, ensure_config]
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/_internal/_config.py#L334)
