---
title: "LLMResult"
description: "A container for results of an LLM call."
source: "https://reference.langchain.com/python/langchain-core/outputs/llm_result/LLMResult"
category: "reference"
tags: [reference, langchain-core, outputs, llm_result, llmresult]
---

# LLMResult

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/outputs/llm_result/LLMResult)

A container for results of an LLM call.

Both chat models and LLMs generate an `LLMResult` object. This object contains the
generated outputs and any additional information that the model provider wants to
return.

## Signature

```python
LLMResult()
```

## Extends

- `BaseModel`

## Properties

- `generations`
- `llm_output`
- `run`
- `type`

## Methods

- [`flatten()`](https://reference.langchain.com/python/langchain-core/outputs/llm_result/LLMResult/flatten)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/bdf0f53ed0aec3c9ae371a549e1a4d2ee4e9f021/libs/core/langchain_core/outputs/llm_result.py#L15)
