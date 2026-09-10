---
title: "tags"
description: "Optional list of tags associated with the tool."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/tags"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, tags]
---

# tags

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/tags)

Optional list of tags associated with the tool.

These tags will be associated with each call to this tool,
and passed as arguments to the handlers defined in `callbacks`.

You can use these to, e.g., identify a specific instance of a tool with its use
case.

## Signature

```python
tags: list[str] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tools/base.py#L508)
