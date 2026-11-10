---
title: "on_text"
description: "Run when a text is received."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_text"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, runmanager, on_text]
---

# on_text

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/RunManager/on_text)

Run when a text is received.

## Signature

```python
on_text(
    self,
    text: str,
    kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The received text. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/1a41b51b0295d7cc6df45cdede199b4a34649b1d/libs/core/langchain_core/callbacks/manager.py#L560)
