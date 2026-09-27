---
title: "set_handlers"
description: "Set handlers as the only handlers on the callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/set_handlers"
category: "reference"
tags: [reference, langchain-core, callbacks, base, basecallbackmanager, set_handlers]
---

# set_handlers

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/BaseCallbackManager/set_handlers)

Set handlers as the only handlers on the callback manager.

## Signature

```python
set_handlers(
    self,
    handlers: list[BaseCallbackHandler],
    inherit: bool = True,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `handlers` | `list[BaseCallbackHandler]` | Yes | The handlers to set. |
| `inherit` | `bool` | No | Whether to inherit the handlers. (default: `True`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/callbacks/base.py#L1138)
