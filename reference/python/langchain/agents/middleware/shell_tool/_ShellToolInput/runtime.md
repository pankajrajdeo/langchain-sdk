---
title: "runtime"
description: "The runtime for the shell tool."
source: "https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/_ShellToolInput/runtime"
category: "reference"
tags: [reference, langchain, agents, middleware, shell_tool, shelltoolinput, runtime]
---

# runtime

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/_ShellToolInput/runtime)

The runtime for the shell tool.

Included as a workaround at the moment bc args_schema doesn't work with
injected ToolRuntime.

## Signature

```python
runtime: Annotated[Any, SkipJsonSchema()] = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c0344e0cee824c1c6489ba972cea171ff193d234/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L500)
