---
title: "BinaryOperatorAggregate"
description: "Stores the result of applying a binary operator to the current value and each new value."
source: "https://reference.langchain.com/python/langgraph/channels/binop/BinaryOperatorAggregate"
category: "reference"
tags: [reference, langgraph, channels, binop, binaryoperatoraggregate]
---

# BinaryOperatorAggregate

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/binop/BinaryOperatorAggregate)

Stores the result of applying a binary operator to the current value and each new value.

```python
import operator

total = Channels.BinaryOperatorAggregate(int, operator.add)
```

## Signature

```python
BinaryOperatorAggregate(
    self,
    typ: type[Value],
    operator: Callable[[Value, Value], Value],
)
```

## Extends

- `Generic[Value]`
- `BaseChannel[Value, Value, Value]`

## Constructors

```python
__init__(
    self,
    typ: type[Value],
    operator: Callable[[Value, Value], Value],
)
```

| Name | Type |
|------|------|
| `typ` | `type[Value]` |
| `operator` | `Callable[[Value, Value], Value]` |

## Properties

- `operator`
- `value`
- `ValueType`
- `UpdateType`

## Methods

- [`copy()`](https://reference.langchain.com/python/langgraph/channels/binop/BinaryOperatorAggregate/copy)
- [`from_checkpoint()`](https://reference.langchain.com/python/langgraph/channels/binop/BinaryOperatorAggregate/from_checkpoint)
- [`update()`](https://reference.langchain.com/python/langgraph/channels/binop/BinaryOperatorAggregate/update)
- [`get()`](https://reference.langchain.com/python/langgraph/channels/binop/BinaryOperatorAggregate/get)
- [`is_available()`](https://reference.langchain.com/python/langgraph/channels/binop/BinaryOperatorAggregate/is_available)
- [`checkpoint()`](https://reference.langchain.com/python/langgraph/channels/binop/BinaryOperatorAggregate/checkpoint)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/channels/binop.py#L66)
