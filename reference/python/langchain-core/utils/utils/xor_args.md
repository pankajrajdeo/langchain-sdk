---
title: "xor_args"
description: "Validate specified keyword args are mutually exclusive."
source: "https://reference.langchain.com/python/langchain-core/utils/utils/xor_args"
category: "reference"
tags: [reference, langchain-core, utils, xor_args]
---

# xor_args

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/xor_args)

Validate specified keyword args are mutually exclusive.

## Signature

```python
xor_args(
    arg_groups: tuple[str, ...] = (),
) -> Callable[..., Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `*arg_groups` | `tuple[str, ...]` | No | Groups of mutually exclusive keyword args. (default: `()`) |

## Returns

`Callable[..., Any]`

Decorator that validates the specified keyword args are mutually exclusive.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/utils/utils.py#L24)
