---
title: "l_sa_check"
description: "Do a preliminary check to see if a tag could be a standalone."
source: "https://reference.langchain.com/python/langchain-core/utils/mustache/l_sa_check"
category: "reference"
tags: [reference, langchain-core, utils, mustache, l_sa_check]
---

# l_sa_check

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/mustache/l_sa_check)

Do a preliminary check to see if a tag could be a standalone.

## Signature

```python
l_sa_check(
    template: str,
    literal: str,
    is_standalone: bool,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | The template. (Not used.) |
| `literal` | `str` | Yes | The literal. |
| `is_standalone` | `bool` | Yes | Whether the tag is standalone. |

## Returns

`bool`

Whether the tag could be a standalone.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/mustache.py#L66)
