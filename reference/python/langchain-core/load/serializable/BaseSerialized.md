---
title: "BaseSerialized"
description: "Base class for serialized objects."
source: "https://reference.langchain.com/python/langchain-core/load/serializable/BaseSerialized"
category: "reference"
tags: [reference, langchain-core, load, serializable, baseserialized]
---

# BaseSerialized

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/serializable/BaseSerialized)

Base class for serialized objects.

## Signature

```python
BaseSerialized()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    lc: int,
    id: list[str],
    name: NotRequired[str],
    graph: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `lc` | `int` |
| `id` | `list[str]` |
| `name` | `NotRequired[str]` |
| `graph` | `NotRequired[dict[str, Any]]` |

## Properties

- `lc`
- `id`
- `name`
- `graph`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/load/serializable.py#L21)
