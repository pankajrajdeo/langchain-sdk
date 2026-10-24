---
title: "is_invalid_resume"
description: "Whether error was raised because a resume value didn't match response_schema."
source: "https://reference.langchain.com/python/langgraph/errors/is_invalid_resume"
category: "reference"
tags: [reference, langgraph, errors, is_invalid_resume]
---

# is_invalid_resume

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/errors/is_invalid_resume)

Whether `error` was raised because a resume value didn't match `response_schema`.

`interrupt()` raises a `pydantic.ValidationError` in that case. `ToolNode` uses
this to tell it apart from invalid tool arguments when a tool calls `interrupt()`
or runs a graph that does, so the resume fails and the interrupt can be answered
again.

## Signature

```python
is_invalid_resume(
    error: BaseException,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/errors.py#L252)
