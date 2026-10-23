---
title: "tools"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/tools"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, filesystemmiddleware, tools]
---

# tools

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/filesystem/FilesystemMiddleware/tools)

## Signature

```python
tools = [factory() for name, factory in tool_factories if self._enabled_tools is None or name in self._enabled_tools]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/filesystem.py#L2033)
