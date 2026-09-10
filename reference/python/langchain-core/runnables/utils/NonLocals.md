---
title: "NonLocals"
description: "Get nonlocal variables accessed."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/NonLocals"
category: "reference"
tags: [reference, langchain-core, runnables, utils, nonlocals]
---

# NonLocals

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/NonLocals)

Get nonlocal variables accessed.

## Signature

```python
NonLocals(
    self,
)
```

## Extends

- `ast.NodeVisitor`

## Constructors

```python
__init__(
    self,
) -> None
```

## Properties

- `loads`
- `stores`

## Methods

- [`visit_Name()`](https://reference.langchain.com/python/langchain-core/runnables/utils/NonLocals/visit_Name)
- [`visit_Attribute()`](https://reference.langchain.com/python/langchain-core/runnables/utils/NonLocals/visit_Attribute)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/utils.py#L255)
