---
title: "set_config_context"
description: "Set the child Runnable config + tracing context."
source: "https://reference.langchain.com/python/langgraph/_internal/_runnable/set_config_context"
category: "reference"
tags: [reference, langgraph, internal, runnable, set_config_context]
---

# set_config_context

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_runnable/set_config_context)

Set the child Runnable config + tracing context.

## Signature

```python
set_config_context(
    config: RunnableConfig,
    run: Any = None,
) -> Generator[Context, None, None]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | The config to set. |

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/_internal/_runnable.py#L126)
