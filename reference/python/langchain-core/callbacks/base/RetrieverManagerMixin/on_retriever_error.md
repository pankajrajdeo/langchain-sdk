---
title: "on_retriever_error"
description: "Run when Retriever errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/RetrieverManagerMixin/on_retriever_error"
category: "reference"
tags: [reference, langchain-core, callbacks, base, retrievermanagermixin, on_retriever_error]
---

# on_retriever_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/RetrieverManagerMixin/on_retriever_error)

Run when `Retriever` errors.

## Signature

```python
on_retriever_error(
    self,
    error: BaseException,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error that occurred. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/callbacks/base.py#L27)
