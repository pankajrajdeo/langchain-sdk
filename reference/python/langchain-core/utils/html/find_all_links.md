---
title: "find_all_links"
description: "Extract all links from a raw HTML string."
source: "https://reference.langchain.com/python/langchain-core/utils/html/find_all_links"
category: "reference"
tags: [reference, langchain-core, utils, html, find_all_links]
---

# find_all_links

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/html/find_all_links)

Extract all links from a raw HTML string.

## Signature

```python
find_all_links(
    raw_html: str,
    *,
    pattern: str | re.Pattern[str] | None = None,
) -> list[str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `raw_html` | `str` | Yes | original HTML. |
| `pattern` | `str \| re.Pattern[str] \| None` | No | Regex to use for extracting links from raw HTML. (default: `None`) |

## Returns

`list[str]`

A list of all links found in the HTML.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/utils/html.py#L46)
