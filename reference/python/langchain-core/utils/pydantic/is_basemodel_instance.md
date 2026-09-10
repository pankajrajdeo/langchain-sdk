---
title: "is_basemodel_instance"
description: "Check if the given class is an instance of Pydantic BaseModel."
source: "https://reference.langchain.com/python/langchain-core/utils/pydantic/is_basemodel_instance"
category: "reference"
tags: [reference, langchain-core, utils, pydantic, is_basemodel_instance]
---

# is_basemodel_instance

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/pydantic/is_basemodel_instance)

Check if the given class is an instance of Pydantic `BaseModel`.

Check if the given class is an instance of any of the following:

* `pydantic.BaseModel` in Pydantic 2.x
* `pydantic.v1.BaseModel` in Pydantic 2.x

## Signature

```python
is_basemodel_instance(
    obj: Any,
) -> bool
```

## Returns

`bool`

`True` if the given class is an instance of Pydantic `BaseModel`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/pydantic.py#L115)
