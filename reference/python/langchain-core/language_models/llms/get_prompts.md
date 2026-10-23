---
title: "get_prompts"
description: "Get prompts that are already cached."
source: "https://reference.langchain.com/python/langchain-core/language_models/llms/get_prompts"
category: "reference"
tags: [reference, langchain-core, language_models, llms, get_prompts]
---

# get_prompts

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/llms/get_prompts)

Get prompts that are already cached.

## Signature

```python
get_prompts(
    params: dict[str, Any],
    prompts: list[str],
    cache: BaseCache | bool | None = None,
) -> tuple[dict[int, list[Generation]], str, list[int], list[str]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `params` | `dict[str, Any]` | Yes | Dictionary of parameters. |
| `prompts` | `list[str]` | Yes | List of prompts. |
| `cache` | `BaseCache \| bool \| None` | No | Cache object. (default: `None`) |

## Returns

`tuple[dict[int, list[Generation]], str, list[int], list[str]]`

A tuple of existing prompts, llm_string, missing prompt indexes,
and missing prompts.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/language_models/llms.py#L159)
