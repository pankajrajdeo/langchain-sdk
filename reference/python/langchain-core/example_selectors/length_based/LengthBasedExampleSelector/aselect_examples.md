---
title: "aselect_examples"
description: "Async select which examples to use based on the input lengths."
source: "https://reference.langchain.com/python/langchain-core/example_selectors/length_based/LengthBasedExampleSelector/aselect_examples"
category: "reference"
tags: [reference, langchain-core, example_selectors, length_based, lengthbasedexampleselector, aselect_examples]
---

# aselect_examples

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/example_selectors/length_based/LengthBasedExampleSelector/aselect_examples)

Async select which examples to use based on the input lengths.

## Signature

```python
aselect_examples(
    self,
    input_variables: dict[str, str],
) -> list[dict[str, Any]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input_variables` | `dict[str, str]` | Yes | A dictionary with keys as input variables and values as their values. |

## Returns

`list[dict[str, Any]]`

A list of examples to include in the prompt.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/example_selectors/length_based.py#L119)
