---
title: "aformat"
description: "Async format the prompt with the inputs."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/aformat"
category: "reference"
tags: [reference, langchain-core, prompts, base, baseprompttemplate, aformat]
---

# aformat

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/prompts/base/BasePromptTemplate/aformat)

Async format the prompt with the inputs.

## Signature

```python
aformat(
    self,
    kwargs: Any = {},
) -> FormatOutputType
```

## Description

**Example:**

```python
await prompt.aformat(variable1="foo")
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `**kwargs` | `Any` | No | Any arguments to be passed to the prompt template. (default: `{}`) |

## Returns

`FormatOutputType`

A formatted string.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/prompts/base.py#L332)
