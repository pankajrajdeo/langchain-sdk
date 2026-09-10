---
title: "patch_config"
description: "Patch a config with new values."
source: "https://reference.langchain.com/python/langchain-core/runnables/fallbacks/patch_config"
category: "reference"
tags: [reference, langchain-core, runnables, fallbacks, patch_config]
---

# patch_config

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/patch_config)

Patch a config with new values.

## Signature

```python
patch_config(
    config: RunnableConfig | None,
    *,
    callbacks: BaseCallbackManager | None = None,
    recursion_limit: int | None = None,
    max_concurrency: int | None = None,
    run_name: str | None = None,
    configurable: dict[str, Any] | None = None,
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | Yes | The config to patch. |
| `callbacks` | `BaseCallbackManager \| None` | No | The callbacks to set. (default: `None`) |
| `recursion_limit` | `int \| None` | No | The recursion limit to set. (default: `None`) |
| `max_concurrency` | `int \| None` | No | The max concurrency to set. (default: `None`) |
| `run_name` | `str \| None` | No | The run name to set. (default: `None`) |
| `configurable` | `dict[str, Any] \| None` | No | The configurable to set. (default: `None`) |

## Returns

`RunnableConfig`

The patched config.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/config.py#L357)
