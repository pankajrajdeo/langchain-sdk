---
title: "score"
description: "Score pairs' similarity."
source: "https://reference.langchain.com/python/langchain-core/cross_encoders/BaseCrossEncoder/score"
category: "reference"
tags: [reference, langchain-core, cross_encoders, basecrossencoder, score]
---

# score

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/cross_encoders/BaseCrossEncoder/score)

Score pairs' similarity.

## Signature

```python
score(
    self,
    text_pairs: list[tuple[str, str]],
) -> list[float]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text_pairs` | `list[tuple[str, str]]` | Yes | List of pairs of texts. |

## Returns

`list[float]`

List of scores.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/cross_encoders.py#L9)
