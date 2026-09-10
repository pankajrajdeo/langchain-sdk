---
title: "on_llm_new_token"
description: "Run when LLM generates a new token."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForLLMRun/on_llm_new_token"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asynccallbackmanagerforllmrun, on_llm_new_token]
---

# on_llm_new_token

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncCallbackManagerForLLMRun/on_llm_new_token)

Run when LLM generates a new token.

## Signature

```python
on_llm_new_token(
    self,
    token: str | list[str | dict[str, Any]],
    *,
    chunk: GenerationChunk | ChatGenerationChunk | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `token` | `str \| list[str \| dict[str, Any]]` | Yes | The new token, or a list of content blocks. |
| `chunk` | `GenerationChunk \| ChatGenerationChunk \| None` | No | The chunk. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/manager.py#L827)
