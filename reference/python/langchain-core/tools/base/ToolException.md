---
title: "ToolException"
description: "Exception thrown when a tool execution error occurs."
source: "https://reference.langchain.com/python/langchain-core/tools/base/ToolException"
category: "reference"
tags: [reference, langchain-core, tools, base, toolexception]
---

# ToolException

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/ToolException)

Exception thrown when a tool execution error occurs.

This exception allows tools to signal errors without stopping the agent.

The error is handled according to the tool's `handle_tool_error` setting, and the
result is returned as an observation to the agent.

## Signature

```python
ToolException()
```

## Extends

- `Exception`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/tools/base.py#L372)
