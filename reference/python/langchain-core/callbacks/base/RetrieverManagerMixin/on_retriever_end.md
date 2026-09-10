---
title: "on_retriever_end"
description: "Run when Retriever ends running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/RetrieverManagerMixin/on_retriever_end"
category: "reference"
tags: [reference, langchain-core, callbacks, base, retrievermanagermixin, on_retriever_end]
---

# on_retriever_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/RetrieverManagerMixin/on_retriever_end)

Run when `Retriever` ends running.

## Signature

```python
on_retriever_end(
    self,
    documents: Sequence[Document],
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `documents` | `Sequence[Document]` | Yes | The documents retrieved. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/base.py#L44)
