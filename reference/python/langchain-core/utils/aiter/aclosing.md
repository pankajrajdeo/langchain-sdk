---
title: "aclosing"
description: "Async context manager to wrap an AsyncGenerator that has a aclose() method."
source: "https://reference.langchain.com/python/langchain-core/utils/aiter/aclosing"
category: "reference"
tags: [reference, langchain-core, utils, aiter, aclosing]
---

# aclosing

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/aiter/aclosing)

Async context manager to wrap an `AsyncGenerator` that has a `aclose()` method.

Code like this:

```python
async with aclosing(<module>.fetch(<arguments>)) as agen:
    <block>
```

...is equivalent to this:

```python
agen = <module>.fetch(<arguments>)
try:
    <block>
finally:
    await agen.aclose()

```

## Signature

```python
aclosing(
    self,
    thing: AsyncGenerator[Any, Any] | AsyncIterator[Any],
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `thing` | `AsyncGenerator[Any, Any] \| AsyncIterator[Any]` | Yes | The resource to wrap. |

## Extends

- `AbstractAsyncContextManager[Any]`

## Constructors

```python
__init__(
    self,
    thing: AsyncGenerator[Any, Any] | AsyncIterator[Any],
) -> None
```

| Name | Type |
|------|------|
| `thing` | `AsyncGenerator[Any, Any] \| AsyncIterator[Any]` |

## Properties

- `thing`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/utils/aiter.py#L280)
