---
title: "on_tool_error"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/on_tool_error"
category: "reference"
tags: [reference, langgraph, pregel, tools, streamtoolcallhandler, on_tool_error]
---

# on_tool_error

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/on_tool_error)

## Signature

```python
on_tool_error(
    self,
    error: BaseException,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    kwargs: Any = {},
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_tools.py#L260)
