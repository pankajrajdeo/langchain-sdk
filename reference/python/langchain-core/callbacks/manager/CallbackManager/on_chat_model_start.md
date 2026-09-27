---
title: "on_chat_model_start"
description: "Run when chat model starts running."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_chat_model_start"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanager, on_chat_model_start]
---

# on_chat_model_start

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/on_chat_model_start)

Run when chat model starts running.

## Signature

```python
on_chat_model_start(
    self,
    serialized: dict[str, Any],
    messages: list[list[BaseMessage]],
    run_id: UUID | None = None,
    **kwargs: Any = {},
) -> list[CallbackManagerForLLMRun]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `serialized` | `dict[str, Any]` | Yes | The serialized LLM. |
| `messages` | `list[list[BaseMessage]]` | Yes | The list of messages. |
| `run_id` | `UUID \| None` | No | The ID of the run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

## Returns

`list[CallbackManagerForLLMRun]`

A callback manager for each list of messages as an LLM run.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/callbacks/manager.py#L1431)
