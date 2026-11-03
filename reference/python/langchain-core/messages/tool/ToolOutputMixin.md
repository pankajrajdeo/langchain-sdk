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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/messages/tool.py#L16)
