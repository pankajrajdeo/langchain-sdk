---
title: "grab_literal"
description: "Parse a literal from the template."
source: "https://reference.langchain.com/python/langchain-core/utils/mustache/grab_literal"
category: "reference"
tags: [reference, langchain-core, utils, mustache, grab_literal]
---

# grab_literal

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/mustache/grab_literal)

Parse a literal from the template.

## Signature

```python
grab_literal(
    template: str,
    l_del: str,
) -> tuple[str, str]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template to parse. |
| `l_del` | `str` | Yes | The left delimiter. |

## Returns

`tuple[str, str]`

The literal and the template.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/utils/mustache.py#L41)
