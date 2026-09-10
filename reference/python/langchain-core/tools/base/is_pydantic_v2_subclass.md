---
title: "is_pydantic_v2_subclass"
description: "Check if the given class is Pydantic v2-like."
source: "https://reference.langchain.com/python/langchain-core/tools/base/is_pydantic_v2_subclass"
category: "reference"
tags: [reference, langchain-core, tools, base, is_pydantic_v2_subclass]
---

# is_pydantic_v2_subclass

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/is_pydantic_v2_subclass)

Check if the given class is Pydantic v2-like.

## Signature

```python
is_pydantic_v2_subclass(
    cls: type,
) -> TypeGuard[type[BaseModel]]
```

## Returns

`TypeGuard[type[BaseModel]]`

`True` if the given class is a subclass of Pydantic `BaseModel` 2.x.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/pydantic.py#L88)
