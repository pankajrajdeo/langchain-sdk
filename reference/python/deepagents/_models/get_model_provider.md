---
title: "get_model_provider"
description: "Extract the provider name from a chat model instance."
source: "https://reference.langchain.com/python/deepagents/_models/get_model_provider"
category: "reference"
tags: [reference, deepagents, models, get_model_provider]
---

# get_model_provider

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/_models/get_model_provider)

Extract the provider name from a chat model instance.

Uses the model's `_get_ls_params` method. The base `BaseChatModel`
implementation derives `ls_provider` from the class name, and all major
providers override it with a hardcoded value (e.g. `"anthropic"`).

## Signature

```python
get_model_provider(
    model: BaseChatModel,
) -> str | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `BaseChatModel` | Yes | Chat model instance to inspect. |

## Returns

`str | None`

The provider name, or `None` if unavailable.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/_models.py#L75)
