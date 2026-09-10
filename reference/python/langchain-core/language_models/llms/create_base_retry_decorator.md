---
title: "create_base_retry_decorator"
description: "Create a retry decorator for a given LLM and provided a list of error types."
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/create_base_retry_decorator"
category: "reference"
tags: [reference, langchain-core, language_models, llms, create_base_retry_decorator]
---

# create_base_retry_decorator

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/create_base_retry_decorator)

Create a retry decorator for a given LLM and provided a list of error types.

## Signature

```python
create_base_retry_decorator(
    error_types: list[type[BaseException]],
    max_retries: int = 1,
    run_manager: AsyncCallbackManagerForLLMRun | CallbackManagerForLLMRun | None = None,
) -> Callable[[Any], Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `error_types` | `list[type[BaseException]]` | Yes | List of error types to retry on. |
| `max_retries` | `int` | No | Number of retries. (default: `1`) |
| `run_manager` | `AsyncCallbackManagerForLLMRun \| CallbackManagerForLLMRun \| None` | No | Callback manager for the run. (default: `None`) |

## Returns

`Callable[[Any], Any]`

A retry decorator.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/llms.py#L77)
