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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/utils.py#L307)
