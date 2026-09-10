---
title: "InitValidator"
description: "Type alias for a callable that validates kwargs during deserialization."
source: "https://reference.langchain.com/python/langchain-core/load/load/InitValidator"
category: "reference"
tags: [reference, langchain-core, load, initvalidator]
---

# InitValidator

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/load/load/InitValidator)

Type alias for a callable that validates kwargs during deserialization.

The callable receives:

- `class_path`: A tuple of strings identifying the class being instantiated
    (e.g., `('langchain', 'schema', 'messages', 'AIMessage')`).
- `kwargs`: The kwargs dict that will be passed to the constructor.

The validator should raise an exception if the object should not be deserialized.

## Signature

```python
InitValidator = Callable[[tuple[str, ...], dict[str, Any]], None]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/load/load.py#L276)
