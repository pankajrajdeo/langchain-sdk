---
title: "batch_iterate"
description: "Utility batching function."
source: "https://reference.langchain.com/python/langchain-core/utils/iter/batch_iterate"
category: "reference"
tags: [reference, langchain-core, utils, iter, batch_iterate]
---

# batch_iterate

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/iter/batch_iterate)

Utility batching function.

## Signature

```python
batch_iterate(
    size: int | None,
    iterable: Iterable[T],
) -> Iterator[list[T]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `size` | `int \| None` | Yes | The size of the batch.  If `None`, returns a single batch. |
| `iterable` | `Iterable[T]` | Yes | The iterable to batch. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/utils/iter.py#L206)
