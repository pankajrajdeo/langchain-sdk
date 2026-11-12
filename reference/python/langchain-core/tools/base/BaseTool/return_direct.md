---
title: "return_direct"
description: "Whether to return the tool's output directly."
source: "https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/return_direct"
category: "reference"
tags: [reference, langchain-core, tools, base, basetool, return_direct]
---

# return_direct

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/BaseTool/return_direct)

Whether to return the tool's output directly.

Setting this to `True` means that after the tool is called, the `AgentExecutor` will
stop looping.

## Signature

```python
return_direct: bool = False
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/tools/base.py#L496)
