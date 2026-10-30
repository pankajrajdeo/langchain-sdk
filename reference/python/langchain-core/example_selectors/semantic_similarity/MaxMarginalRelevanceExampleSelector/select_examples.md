---
title: "select_examples"
description: "Select examples based on Max Marginal Relevance."
source: "https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector/select_examples"
category: "reference"
tags: [reference, langchain-core, example_selectors, semantic_similarity, maxmarginalrelevanceexampleselector, select_examples]
---

# select_examples

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/example_selectors/semantic_similarity/MaxMarginalRelevanceExampleSelector/select_examples)

Select examples based on Max Marginal Relevance.

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
| `input_variables` | `dict[str, str]` | Yes | The input variables to use for search. |

## Returns

`list[dict[str, Any]]`

The selected examples.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/example_selectors/semantic_similarity.py#L241)
