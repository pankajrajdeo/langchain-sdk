---
title: "ToolExceptionHandlerOutput"
description: "Type Alias in langchain_core"
source: "https://reference.langchain.com/python/langchain-core/tools/base/ToolExceptionHandlerOutput"
category: "reference"
tags: [reference, langchain-core, tools, base, toolexceptionhandleroutput]
---

# ToolExceptionHandlerOutput

> **Type Alias** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tools/base/ToolExceptionHandlerOutput)

Content returned by a `handle_tool_error` callable.

Error handlers may return plain text or a sequence of structured message
content blocks. When the original tool call includes a `tool_call_id`, this
content is normalized to the content of a `ToolMessage` with `status="error"`.

## Signature

```python
ToolExceptionHandlerOutput = str | Sequence[MessageContentBlock]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/tools/base.py#L389)
