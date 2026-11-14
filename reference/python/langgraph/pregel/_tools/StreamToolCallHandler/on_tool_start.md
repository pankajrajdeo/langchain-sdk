---
title: "on_tool_start"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/on_tool_start"
category: "reference"
tags: [reference, langgraph, pregel, tools, streamtoolcallhandler, on_tool_start]
---

# on_tool_start

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_tools/StreamToolCallHandler/on_tool_start)

## Signature

```python
on_tool_start(
    self,
    serialized: dict[str, Any],
    input_str: str,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inputs: dict[str, Any] | None = None,
    kwargs: Any = {},
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/pregel/_tools.py#L228)
