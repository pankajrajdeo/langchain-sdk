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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/runnables/utils.py#L212)
