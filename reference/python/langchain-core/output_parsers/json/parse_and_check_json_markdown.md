---
title: "parse_and_check_json_markdown"
description: "Parse and check a JSON string from a Markdown string."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/json/parse_and_check_json_markdown"
category: "reference"
tags: [reference, langchain-core, output_parsers, json, parse_and_check_json_markdown]
---

# parse_and_check_json_markdown

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/json/parse_and_check_json_markdown)

Parse and check a JSON string from a Markdown string.

Checks that it contains the expected keys.

## Signature

```python
parse_and_check_json_markdown(
    text: str,
    expected_keys: list[str],
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `text` | `str` | Yes | The Markdown string. |
| `expected_keys` | `list[str]` | Yes | The expected keys in the JSON string. |

## Returns

`dict[str, Any]`

The parsed JSON object as a Python dictionary.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/json.py#L194)
