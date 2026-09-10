---
title: "on_text"
description: "Run when a text is received."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncRunManager/on_text"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asyncrunmanager, on_text]
---

# on_text

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncRunManager/on_text)

Run when a text is received.

## Signature

```python
on_text(
    self,
    text: str,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The received text. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L633)
