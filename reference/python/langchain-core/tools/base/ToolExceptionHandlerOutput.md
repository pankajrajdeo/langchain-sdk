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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tools/base.py#L389)
