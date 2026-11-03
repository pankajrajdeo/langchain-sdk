---
title: "on_tool_error"
description: "Run when tool errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForToolRun/on_tool_error"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerfortoolrun, on_tool_error]
---

# on_tool_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForToolRun/on_tool_error)

Run when tool errors.

## Signature

```python
on_tool_error(
    self,
    error: BaseException,
    kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/callbacks/manager.py#L1166)
