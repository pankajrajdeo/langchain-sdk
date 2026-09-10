---
title: "select_examples"
description: "Select which examples to use based on the inputs."
source: "https://reference.langchain.com/python/langchain-core/example_selectors/base/BaseExampleSelector/select_examples"
category: "reference"
tags: [reference, langchain-core, example_selectors, base, baseexampleselector, select_examples]
---

# select_examples

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/example_selectors/base/BaseExampleSelector/select_examples)

Select which examples to use based on the inputs.

## Signature

```python
select_examples(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/example_selectors/base.py#L36)
