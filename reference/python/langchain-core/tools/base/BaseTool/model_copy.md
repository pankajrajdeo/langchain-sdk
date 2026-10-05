---
title: "model_copy"
description: "Copy the tool, clearing the schema memo if update affects it."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/model_copy"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, model_copy]
---

# model_copy

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/model_copy)

Copy the tool, clearing the schema memo if `update` affects it.

`model_copy` writes `update` directly to the copy's `__dict__` without
going through `__setattr__`, and private attributes (including the
memo) carry over to the copy, so the memo is cleared here when the
update touches one of the fields the schema is built from.

## Signature

```python
model_copy(
    self,
    *,
    update: Mapping[str, Any] | None = None,
    deep: bool = False,
) -> Self
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/tools/base.py#L644)
