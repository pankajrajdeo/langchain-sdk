---
title: "guard_import"
description: "Dynamically import a module."
source: "https://reference.langchain.com/python/langchain-core/utils/utils/guard_import"
category: "reference"
tags: [reference, langchain-core, utils, guard_import]
---

# guard_import

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/guard_import)

Dynamically import a module.

Raise an exception if the module is not installed.

## Signature

```python
guard_import(
    module_name: str,
    *,
    pip_name: str | None = None,
    package: str | None = None,
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `module_name` | `str` | Yes | The name of the module to import. |
| `pip_name` | `str \| None` | No | The name of the module to install with pip. (default: `None`) |
| `package` | `str \| None` | No | The package to import the module from. (default: `None`) |

## Returns

`Any`

The imported module.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/utils/utils.py#L116)
