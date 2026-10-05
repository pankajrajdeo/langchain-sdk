---
title: "get_executor_for_config"
description: "Get an executor for a config."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/get_executor_for_config"
category: "reference"
tags: [reference, langchain-core, runnables, base, get_executor_for_config]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/runnables/config.py#L659)
