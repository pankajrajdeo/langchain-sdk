---
title: "get_graph"
description: "Get the graph representation of the Runnable."
source: "https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_graph"
category: "reference"
tags: [reference, langchain-core, runnables, base, runnableparallel, get_graph]
---

# get_graph

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/base/RunnableParallel/get_graph)

Get the graph representation of the `Runnable`.

## Signature

```python
get_graph(
    self,
    config: RunnableConfig | None = None,
) -> Graph
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `config` | `RunnableConfig \| None` | No | The config to use. (default: `None`) |

## Returns

`Graph`

The graph representation of the `Runnable`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/runnables/base.py#L4110)
