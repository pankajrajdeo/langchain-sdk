---
title: "prefix_config_spec"
description: "Prefix the id of a ConfigurableFieldSpec."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/prefix_config_spec"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, prefix_config_spec]
---

# prefix_config_spec

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/prefix_config_spec)

Prefix the id of a `ConfigurableFieldSpec`.

This is useful when a `RunnableConfigurableAlternatives` is used as a
`ConfigurableField` of another `RunnableConfigurableAlternatives`.

## Signature

```python
prefix_config_spec(
    spec: ConfigurableFieldSpec,
    prefix: str,
) -> ConfigurableFieldSpec
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `spec` | `ConfigurableFieldSpec` | Yes | The `ConfigurableFieldSpec` to prefix. |
| `prefix` | `str` | Yes | The prefix to add. |

## Returns

`ConfigurableFieldSpec`

The prefixed `ConfigurableFieldSpec`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/configurable.py#L640)
