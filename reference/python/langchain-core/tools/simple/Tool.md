---
title: "Tool"
description: "Tool that takes in function or coroutine directly."
source: "https://reference.langchain.com/python/langchain-core/tools/simple/Tool"
category: "reference"
tags: [reference, langchain-core, tools, simple, tool]
---

# Tool

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/simple/Tool)

Tool that takes in function or coroutine directly.

## Signature

```python
Tool(
    self,
    name: str,
    func: Callable[..., Any] | None,
    description: str,
    **kwargs: Any = {},
)
```

## Extends

- `BaseTool`

## Constructors

```python
__init__(
    self,
    name: str,
    func: Callable[..., Any] | None,
    description: str,
    **kwargs: Any = {},
) -> None
```

| Name | Type |
|------|------|
| `name` | `str` |
| `func` | `Callable[..., Any] \| None` |
| `description` | `str` |

## Properties

- `description`
- `func`
- `coroutine`
- `args`

## Methods

- [`ainvoke()`](https://reference.langchain.com/python/langchain-core/tools/simple/Tool/ainvoke)
- [`from_function()`](https://reference.langchain.com/python/langchain-core/tools/simple/Tool/from_function)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tools/simple.py#L31)
