---
title: "lc_id"
description: "Return a unique identifier for this class for serialization purposes."
source: "https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/lc_id"
category: "reference"
tags: [reference, langchain-core, load, serializable, lc_id]
---

# lc_id

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/serializable/Serializable/lc_id)

Return a unique identifier for this class for serialization purposes.

The unique identifier is a list of strings that describes the path
to the object.

For example, for the class `langchain.llms.openai.OpenAI`, the id is
`["langchain", "llms", "openai", "OpenAI"]`.

## Signature

```python
lc_id(
    cls,
) -> list[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/load/serializable.py#L195)
