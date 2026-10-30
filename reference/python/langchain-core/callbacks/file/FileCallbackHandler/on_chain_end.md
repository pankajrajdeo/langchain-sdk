---
title: "on_chain_end"
description: "Print that we finished a chain."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_chain_end"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler, on_chain_end]
---

# on_chain_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_chain_end)

Print that we finished a chain.

## Signature

```python
on_chain_end(
    self,
    outputs: dict[str, Any],
    kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `outputs` | `dict[str, Any]` | Yes | The outputs of the chain. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/callbacks/file.py#L181)
