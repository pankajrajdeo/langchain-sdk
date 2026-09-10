---
title: "ToolOutputMixin"
description: "Mixin for objects that tools can return directly."
source: "https://reference.langchain.com/python/langchain-core/messages/tool/ToolOutputMixin"
category: "reference"
tags: [reference, langchain-core, messages, tool, tooloutputmixin]
---

# ToolOutputMixin

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/tool/ToolOutputMixin)

Mixin for objects that tools can return directly.

If a custom BaseTool is invoked with a `ToolCall` and the output of custom code is
not an instance of `ToolOutputMixin`, the output will automatically be coerced to
a string and wrapped in a `ToolMessage`.

## Signature

```python
ToolOutputMixin()
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/tool.py#L16)
