---
title: "convert_to_secret_str"
description: "Convert a string to a SecretStr if needed."
source: "https://reference.langchain.com/python/langchain-core/utils/utils/convert_to_secret_str"
category: "reference"
tags: [reference, langchain-core, utils, convert_to_secret_str]
---

# convert_to_secret_str

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/convert_to_secret_str)

Convert a string to a `SecretStr` if needed.

## Signature

```python
convert_to_secret_str(
    value: SecretStr | str,
) -> SecretStr
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `value` | `SecretStr \| str` | Yes | The value to convert. |

## Returns

`SecretStr`

The `SecretStr` value.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/utils/utils.py#L313)
