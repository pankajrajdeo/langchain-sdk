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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/runnables/config.py#L659)
