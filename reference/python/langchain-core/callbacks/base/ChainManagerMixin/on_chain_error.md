---
title: "on_chain_error"
description: "Run when chain errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/ChainManagerMixin/on_chain_error"
category: "reference"
tags: [reference, langchain-core, callbacks, base, chainmanagermixin, on_chain_error]
---

# on_chain_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/ChainManagerMixin/on_chain_error)

Run when chain errors.

## Signature

```python
on_chain_error(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/base.py#L189)
