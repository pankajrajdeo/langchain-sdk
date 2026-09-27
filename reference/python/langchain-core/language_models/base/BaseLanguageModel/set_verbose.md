---
title: "set_verbose"
description: "If verbose is None, set it."
source: "https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/set_verbose"
category: "reference"
tags: [reference, langchain-core, language_models, base, baselanguagemodel, set_verbose]
---

# set_verbose

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/language_models/base/BaseLanguageModel/set_verbose)

If verbose is `None`, set it.

This allows users to pass in `None` as verbose to access the global setting.

## Signature

```python
set_verbose(
    cls,
    verbose: bool | None,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `verbose` | `bool \| None` | Yes | The verbosity setting to use. |

## Returns

`bool`

The verbosity setting to use.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/language_models/base.py#L291)
