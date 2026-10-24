---
title: "get_async_callback_manager_for_config"
description: "Get an async callback manager for a config."
source: "https://reference.langchain.com/python/langgraph/_internal/_config/get_async_callback_manager_for_config"
category: "reference"
tags: [reference, langgraph, internal, config, get_async_callback_manager_for_config]
---

# get_async_callback_manager_for_config

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_config/get_async_callback_manager_for_config)

Get an async callback manager for a config.

## Signature

```python
get_async_callback_manager_for_config(
    config: RunnableConfig,
    tags: Sequence[str] | None = None,
) -> AsyncCallbackManager
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | The config. |

## Returns

`AsyncCallbackManager`

The async callback manager.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/_internal/_config.py#L287)
