---
title: "RunnableSerializable"
description: "Runnable that can be serialized to JSON."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSerializable"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableserializable]
---

# RunnableSerializable

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSerializable)

Runnable that can be serialized to JSON.

## Signature

```python
RunnableSerializable(
    self,
    *args: Any = (),
    **kwargs: Any = {},
)
```

## Extends

- `Serializable`
- `Runnable[Input, Output]`

## Properties

- `name`
- `model_config`

## Methods

- [`to_json()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSerializable/to_json)
- [`configurable_fields()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSerializable/configurable_fields)
- [`configurable_alternatives()`](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableSerializable/configurable_alternatives)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/base.py#L2827)
