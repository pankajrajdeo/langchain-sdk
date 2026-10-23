---
title: "parse_with_prompt"
description: "Parse the output of an LLM call with the input prompt for context."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/parse_with_prompt"
category: "reference"
tags: [reference, langchain-core, output_parsers, base, baseoutputparser, parse_with_prompt]
---

# parse_with_prompt

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/parse_with_prompt)

Parse the output of an LLM call with the input prompt for context.

The prompt is largely provided in the event the `OutputParser` wants to retry or
fix the output in some way, and needs information from the prompt to do so.

## Signature

```python
parse_with_prompt(
    self,
    completion: str,
    prompt: PromptValue,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `completion` | `str` | Yes | String output of a language model. |
| `prompt` | `PromptValue` | Yes | Input `PromptValue`. |

## Returns

`Any`

Structured output.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/output_parsers/base.py#L315)
