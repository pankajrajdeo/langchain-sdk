---
title: "try_json_stringify"
description: "Try to stringify an object to JSON."
source: "https://reference.langchain.com/python/langchain-core/tracers/stdout/try_json_stringify"
category: "reference"
tags: [reference, langchain-core, tracers, stdout, try_json_stringify]
---

# try_json_stringify

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/stdout/try_json_stringify)

Try to stringify an object to JSON.

## Signature

```python
try_json_stringify(
    obj: Any,
    fallback: str,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `obj` | `Any` | Yes | Object to stringify. |
| `fallback` | `str` | Yes | Fallback string to return if the object cannot be stringified. |

## Returns

`str`

A JSON string if the object can be stringified, otherwise the fallback string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/tracers/stdout.py#L14)
