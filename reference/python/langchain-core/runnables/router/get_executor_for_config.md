---
title: "get_executor_for_config"
description: "Get an executor for a config."
source: "https://reference.langchain.com/python/langchain-core/runnables/router/get_executor_for_config"
category: "reference"
tags: [reference, langchain-core, runnables, router, get_executor_for_config]
---

# get_executor_for_config

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/get_executor_for_config)

Get an executor for a config.

## Signature

```python
get_executor_for_config(
    config: RunnableConfig | None,
) -> Generator[Executor, None, None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | Yes | The config. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/config.py#L659)
