---
title: "aselect_examples"
description: "Asynchronously select examples based on semantic similarity."
source: "https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/SemanticSimilarityExampleSelector/aselect_examples"
category: "reference"
tags: [reference, langchain-core, example_selectors, semantic_similarity, semanticsimilarityexampleselector, aselect_examples]
---

# aselect_examples

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/SemanticSimilarityExampleSelector/aselect_examples)

Asynchronously select examples based on semantic similarity.

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
| `input_variables` | `dict[str, str]` | Yes | The input variables to use for search. |

## Returns

`list[dict[str, Any]]`

The selected examples.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/example_selectors/semantic_similarity.py#L122)
