---
title: "on_retry"
description: "Run when a retry is received."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_retry"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, runmanager, on_retry]
---

# on_retry

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_retry)

Run when a retry is received.

## Signature

```python
on_retry(
    self,
    retry_state: RetryCallState,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `retry_state` | `RetryCallState` | Yes | The retry state. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/callbacks/manager.py#L573)
