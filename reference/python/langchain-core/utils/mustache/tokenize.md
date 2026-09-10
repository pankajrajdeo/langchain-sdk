---
title: "tokenize"
description: "Tokenize a mustache template."
source: "https://reference.langchain.com/python/langchain-core/utils/mustache/tokenize"
category: "reference"
tags: [reference, langchain-core, utils, mustache, tokenize]
---

# tokenize

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/mustache/tokenize)

Tokenize a mustache template.

Tokenizes a mustache template in a generator fashion, using file-like objects. It
also accepts a string containing the template.

## Signature

```python
tokenize(
    template: str,
    def_ldel: str = '{{',
    def_rdel: str = '}}',
) -> Iterator[tuple[str, str]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `template` | `str` | Yes | a file-like object, or a string of a mustache template |
| `def_ldel` | `str` | No | The default left delimiter (`'{{'` by default, as in spec compliant mustache) (default: `'{{'`) |
| `def_rdel` | `str` | No | The default right delimiter (`'}}'` by default, as in spec compliant mustache) (default: `'}}'`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/mustache.py#L199)
