---
title: "on_llm_error"
description: "Run when LLM errors."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForLLMRun/on_llm_error"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforllmrun, on_llm_error]
---

# on_llm_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForLLMRun/on_llm_error)

Run when LLM errors.

## Signature

```python
on_llm_error(
    self,
    error: BaseException,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error` | `BaseException` | Yes | The error. |
| `**kwargs` | `Any` | No | Additional keyword arguments.  - response (LLMResult): The response which was generated before     the error occurred. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L878)
