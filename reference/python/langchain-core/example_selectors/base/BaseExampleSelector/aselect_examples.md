---
title: "aselect_examples"
description: "Async select which examples to use based on the inputs."
source: "https://reference.langchain.com/python/langchain-core/example_selectors/base/BaseExampleSelector/aselect_examples"
category: "reference"
tags: [reference, langchain-core, example_selectors, base, baseexampleselector, aselect_examples]
---

# aselect_examples

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/example_selectors/base/BaseExampleSelector/aselect_examples)

Async select which examples to use based on the inputs.

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

A list of examples.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/example_selectors/base.py#L48)
