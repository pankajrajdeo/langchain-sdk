---
title: "partial"
description: "Return a partial of the prompt template."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/partial"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, partial]
---

# partial

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/partial)

Return a partial of the prompt template.

## Signature

```python
partial(
    self,
    kwargs: str | Callable[[], str] = {},
) -> BasePromptTemplate[FormatOutputType]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `str \| Callable[[], str]` | No | Partial variables to set. (default: `{}`) |

## Returns

`BasePromptTemplate[FormatOutputType]`

A partial of the prompt template.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/prompts/base.py#L289)
