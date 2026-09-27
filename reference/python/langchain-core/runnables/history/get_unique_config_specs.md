---
title: "get_unique_config_specs"
description: "Get the unique config specs from a sequence of config specs."
source: "https://reference.langchain.com/python/langchain-core/runnables/history/get_unique_config_specs"
category: "reference"
tags: [reference, langchain-core, runnables, history, get_unique_config_specs]
---

# get_unique_config_specs

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/get_unique_config_specs)

Get the unique config specs from a sequence of config specs.

## Signature

```python
get_unique_config_specs(
    specs: Iterable[ConfigurableFieldSpec],
) -> list[ConfigurableFieldSpec]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `specs` | `Iterable[ConfigurableFieldSpec]` | Yes | The config specs. |

## Returns

`list[ConfigurableFieldSpec]`

The unique config specs.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/utils.py#L680)
