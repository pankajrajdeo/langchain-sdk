---
title: "IsFunctionArgDict"
description: "Check if the first argument of a function is a dict."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict"
category: "reference"
tags: [reference, langchain-core, runnables, utils, isfunctionargdict]
---

# IsFunctionArgDict

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict)

Check if the first argument of a function is a dict.

## Signature

```python
IsFunctionArgDict(
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

- `keys`

## Methods

- [`visit_Lambda()`](https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict/visit_Lambda)
- [`visit_FunctionDef()`](https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict/visit_FunctionDef)
- [`visit_AsyncFunctionDef()`](https://reference.langchain.com/python/langchain-core/runnables/utils/IsFunctionArgDict/visit_AsyncFunctionDef)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/runnables/utils.py#L212)
