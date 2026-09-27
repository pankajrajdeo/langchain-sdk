---
title: "dumpd"
description: "Return a dict representation of an object."
source: "https://reference.langchain.com/python/langchain-core/prompts/dict/dumpd"
category: "reference"
tags: [reference, langchain-core, prompts, dict, dumpd]
---

# dumpd

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/dump/dumpd)

Return a dict representation of an object.

## Signature

```python
dumpd(
    obj: Any,
) -> Any
```

## Description

**Note:**

Plain dicts containing an `'lc'` key are automatically escaped to prevent
confusion with LC serialization format. The escape marker is removed during
deserialization.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `obj` | `Any` | Yes | The object to dump. |

## Returns

`Any`

Dictionary that can be serialized to json using `json.dumps`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/load/dump.py#L105)
