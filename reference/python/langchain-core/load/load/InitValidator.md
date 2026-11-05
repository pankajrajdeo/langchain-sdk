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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/load/load.py#L276)
