---
title: "get_config_list"
description: "Get a list of configs from a single config or a list of configs."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/get_config_list"
category: "reference"
tags: [reference, langchain-core, runnables, base, get_config_list]
---

# get_config_list

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/config/get_config_list)

Get a list of configs from a single config or a list of configs.

It is useful for subclasses overriding batch() or abatch().

## Signature

```python
get_config_list(
    config: RunnableConfig | Sequence[RunnableConfig] | None,
    length: int,
) -> list[RunnableConfig]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| Sequence[RunnableConfig] \| None` | Yes | The config or list of configs. |
| `length` | `int` | Yes | The length of the list. |

## Returns

`list[RunnableConfig]`

The list of configs.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/runnables/config.py#L311)
