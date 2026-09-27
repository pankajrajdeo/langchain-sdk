---
title: "metadata"
description: "Optional metadata associated with the tool."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/metadata"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, metadata]
---

# metadata

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/metadata)

Optional metadata associated with the tool.

This metadata will be associated with each call to this tool,
and passed as arguments to the handlers defined in `callbacks`.

You can use these to, e.g., identify a specific instance of a tool with its usecase.

## Signature

```python
metadata: dict[str, Any] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/tools/base.py#L518)
