---
title: "parse"
description: "Parse the output of an LLM call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/list/NumberedListOutputParser/parse"
category: "reference"
tags: [reference, langchain-core, output_parsers, list, numberedlistoutputparser, parse]
---

# parse

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/list/NumberedListOutputParser/parse)

Parse the output of an LLM call.

## Signature

```python
parse(
    self,
    text: str,
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The output of an LLM call. |

## Returns

`list[str]`

A list of strings.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/output_parsers/list.py#L201)
