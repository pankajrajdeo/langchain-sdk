---
title: "on_text"
description: "Handle text output."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_text"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler, on_text]
---

# on_text

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_text)

Handle text output.

## Signature

```python
on_text(
    self,
    text: str,
    color: str | None = None,
    end: str = '',
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The text to write. |
| `color` | `str \| None` | No | Color override for this specific output.  If `None`, uses `self.color`. (default: `None`) |
| `end` | `str` | No | String appended after the text. (default: `''`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/file.py#L236)
