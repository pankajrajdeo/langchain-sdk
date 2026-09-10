---
title: "on_tool_error"
description: "Run when tool errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForToolRun/on_tool_error"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerfortoolrun, on_tool_error]
---

# on_tool_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForToolRun/on_tool_error)

Run when tool errors.

## Signature

```python
on_tool_error(
    self,
    error: BaseException,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L1222)
