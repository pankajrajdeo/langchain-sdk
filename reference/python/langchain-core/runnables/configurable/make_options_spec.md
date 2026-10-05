---
title: "make_options_spec"
description: "Make options spec."
source: "https://reference.langchain.com/python/langchain-core/runnables/configurable/make_options_spec"
category: "reference"
tags: [reference, langchain-core, runnables, configurable, make_options_spec]
---

# make_options_spec

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/configurable/make_options_spec)

Make options spec.

Make a `ConfigurableFieldSpec` for a `ConfigurableFieldSingleOption` or
`ConfigurableFieldMultiOption`.

## Signature

```python
make_options_spec(
    spec: ConfigurableFieldSingleOption | ConfigurableFieldMultiOption,
    description: str | None,
) -> ConfigurableFieldSpec
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `spec` | `ConfigurableFieldSingleOption \| ConfigurableFieldMultiOption` | Yes | The `ConfigurableFieldSingleOption` or `ConfigurableFieldMultiOption`. |
| `description` | `str \| None` | Yes | The description to use if the spec does not have one. |

## Returns

`ConfigurableFieldSpec`

The `ConfigurableFieldSpec`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/runnables/configurable.py#L669)
