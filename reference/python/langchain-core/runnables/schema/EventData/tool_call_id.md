---
title: "tool_call_id"
description: "The tool call ID associated with the tool execution."
source: "https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/tool_call_id"
category: "reference"
tags: [reference, langchain-core, runnables, schema, eventdata, tool_call_id]
---

# tool_call_id

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/schema/EventData/tool_call_id)

The tool call ID associated with the tool execution.

This field is available for the `on_tool_error` event and can be used to
link errors to specific tool calls in stateless agent implementations.

## Signature

```python
tool_call_id: NotRequired[str | None]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/runnables/schema.py#L48)
