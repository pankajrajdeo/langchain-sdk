---
title: "usage"
description: "Token usage reported for the request, or None when not reported."
source: "https://reference.langchain.com/python/langchain-core/decisions/types/ClassifierResponse/usage"
category: "reference"
tags: [reference, langchain-core, decisions, types, classifierresponse, usage]
---

# usage

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/ClassifierResponse/usage)

Token usage reported for the request, or `None` when not reported.

Providers may supply only `input_tokens` and `output_tokens`. A missing count is
treated as `0`, and `total_tokens` defaults to their sum.

## Signature

```python
usage: UsageMetadata | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/decisions/types.py#L349)
