---
title: "create_task_in_config_context"
description: "Create an asyncio.Task that inherits config as the child runnable context."
source: "https://reference.langchain.com/python/langgraph/_internal/_runnable/create_task_in_config_context"
category: "reference"
tags: [reference, langgraph, internal, runnable, create_task_in_config_context]
---

# create_task_in_config_context

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_runnable/create_task_in_config_context)

Create an asyncio.Task that inherits `config` as the child runnable context.

`asyncio.create_task` snapshots the current contextvars onto the new task,
so calling `create_task` while the config context is set ensures the task
sees `config` via `var_child_runnable_config` and any tracing parent.

## Signature

```python
create_task_in_config_context(
    coro_factory: Callable[[], Coroutine[Any, Any, Any]],
    config: RunnableConfig,
) -> asyncio.Task[Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/_internal/_runnable.py#L143)
