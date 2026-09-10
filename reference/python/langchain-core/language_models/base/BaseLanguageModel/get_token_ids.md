---
title: "get_token_ids"
description: "Return the ordered IDs of the tokens in a text."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/get_token_ids"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, get_token_ids]
---

# get_token_ids

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/get_token_ids)

Return the ordered IDs of the tokens in a text.

## Signature

```python
get_token_ids(
    self,
    text: str,
) -> list[int]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The string input to tokenize. |

## Returns

`list[int]`

A list of IDs corresponding to the tokens in the text, in order they occur
in the text.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/language_models/base.py#L434)
