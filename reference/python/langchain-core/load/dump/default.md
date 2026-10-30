---
title: "default"
description: "Return a default value for an object."
source: "https://reference.langchain.com/python/langchain-core/load/dump/default"
category: "reference"
tags: [reference, langchain-core, load, dump, default]
---

# default

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/dump/default)

Return a default value for an object.

## Signature

```python
default(
    obj: Any,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `obj` | `Any` | Yes | The object to serialize to json if it is a Serializable object. |

## Returns

`Any`

A JSON serializable object or a SerializedNotImplemented object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/load/dump.py#L29)
