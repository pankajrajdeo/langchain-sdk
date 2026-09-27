---
title: "FunctionNonLocals"
description: "Get the nonlocal variables accessed of a function."
source: "https://reference.langchain.com/python/langchain-core/runnables/utils/FunctionNonLocals"
category: "reference"
tags: [reference, langchain-core, runnables, utils, functionnonlocals]
---

# FunctionNonLocals

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/utils/FunctionNonLocals)

Get the nonlocal variables accessed of a function.

## Signature

```python
FunctionNonLocals(
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

- `nonlocals`

## Methods

- [`visit_FunctionDef()`](https://reference.langchain.com/python/langchain-core/runnables/utils/FunctionNonLocals/visit_FunctionDef)
- [`visit_AsyncFunctionDef()`](https://reference.langchain.com/python/langchain-core/runnables/utils/FunctionNonLocals/visit_AsyncFunctionDef)
- [`visit_Lambda()`](https://reference.langchain.com/python/langchain-core/runnables/utils/FunctionNonLocals/visit_Lambda)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/utils.py#L307)
