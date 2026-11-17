---
title: "compute_summarization_defaults"
description: "Compute default summarization settings based on model profile."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/compute_summarization_defaults"
category: "reference"
tags: [reference, deepagents, middleware, summarization, compute_summarization_defaults]
---

# compute_summarization_defaults

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/compute_summarization_defaults)

Compute default summarization settings based on model profile.

## Signature

```python
compute_summarization_defaults(
    model: BaseChatModel,
) -> SummarizationDefaults
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `BaseChatModel` | Yes | A resolved chat model instance. |

## Returns

`SummarizationDefaults`

Default settings for trigger, keep, and truncate_args_settings.
If the model has a profile with `max_input_tokens`, uses
fraction-based settings. Otherwise, uses fixed token/message counts.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/middleware/summarization.py#L294)
