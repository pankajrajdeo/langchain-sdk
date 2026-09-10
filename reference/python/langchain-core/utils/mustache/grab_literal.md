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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/mustache.py#L41)
