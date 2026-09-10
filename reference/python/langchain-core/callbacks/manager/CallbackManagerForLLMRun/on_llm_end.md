---
title: "on_llm_end"
description: "Run when LLM ends running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_llm_end"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforllmrun, on_llm_end]
---

# on_llm_end

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForLLMRun/on_llm_end)

Run when LLM ends running.

## Signature

```python
on_llm_end(
    self,
    response: LLMResult,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `response` | `LLMResult` | Yes | The LLM result. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L737)
