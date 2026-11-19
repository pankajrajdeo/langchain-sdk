---
title: "abulk_update_state"
description: "Asynchronously apply updates to the graph state in bulk. Requires a checkpointer to be set."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/abulk_update_state"
category: "reference"
tags: [reference, langgraph, pregel, main, abulk_update_state]
---

# abulk_update_state

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/abulk_update_state)

Asynchronously apply updates to the graph state in bulk. Requires a checkpointer to be set.

## Signature

```python
abulk_update_state(
    self,
    config: RunnableConfig,
    supersteps: Sequence[Sequence[StateUpdate]],
) -> RunnableConfig
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig` | Yes | The config to apply the updates to. |
| `supersteps` | `Sequence[Sequence[StateUpdate]]` | Yes | A list of supersteps, each including a list of updates to apply sequentially to a graph state.  Each update is a tuple of the form `(values, as_node, task_id)` where `task_id` is optional. |

## Returns

`RunnableConfig`

The updated config.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/main.py#L2137)
