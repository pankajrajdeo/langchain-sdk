---
title: "write_todos"
description: "Create and manage a structured task list for your current work session."
source: "https://reference.langchain.com/python/langchain/agents/middleware/todo/write_todos"
category: "reference"
tags: [reference, langchain, agents, middleware, todo, write_todos]
---

# write_todos

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/todo/write_todos)

Create and manage a structured task list for your current work session.

## Signature

```python
write_todos(
    todos: list[Todo],
    tool_call_id: Annotated[str, InjectedToolCallId],
) -> Command[Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/middleware/todo.py#L139)
