---
title: "aparse"
description: "Async parse a single string model output into some structure."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/aparse"
category: "reference"
tags: [reference, langchain-core, output_parsers, base, baseoutputparser, aparse]
---

# aparse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/aparse)

Async parse a single string model output into some structure.

## Signature

```python
aparse(
    self,
    text: str,
) -> T
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | String output of a language model. |

## Returns

`T`

Structured output.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/output_parsers/base.py#L303)
