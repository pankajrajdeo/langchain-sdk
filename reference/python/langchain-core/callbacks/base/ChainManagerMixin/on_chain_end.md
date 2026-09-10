---
title: "on_chain_end"
description: "Run when chain ends running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/ChainManagerMixin/on_chain_end"
category: "reference"
tags: [reference, langchain-core, callbacks, base, chainmanagermixin, on_chain_end]
---

# on_chain_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/ChainManagerMixin/on_chain_end)

Run when chain ends running.

## Signature

```python
on_chain_end(
    self,
    outputs: dict[str, Any],
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `outputs` | `dict[str, Any]` | Yes | The outputs of the chain. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/base.py#L172)
