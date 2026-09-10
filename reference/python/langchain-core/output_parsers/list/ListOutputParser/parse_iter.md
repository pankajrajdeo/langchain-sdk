---
title: "parse_iter"
description: "Parse the output of an LLM call."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/list/ListOutputParser/parse_iter"
category: "reference"
tags: [reference, langchain-core, output_parsers, list, listoutputparser, parse_iter]
---

# parse_iter

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/list/ListOutputParser/parse_iter)

Parse the output of an LLM call.

## Signature

```python
parse_iter(
    self,
    text: str,
) -> Iterator[re.Match[str]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The output of an LLM call. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/output_parsers/list.py#L61)
