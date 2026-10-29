---
title: "get_executor_for_config"
description: "Get an executor for a config."
source: "https://reference.langchain.com/python/langchain-core/runnables/passthrough/get_executor_for_config"
category: "reference"
tags: [reference, langchain-core, runnables, passthrough, get_executor_for_config]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/runnables/config.py#L659)
