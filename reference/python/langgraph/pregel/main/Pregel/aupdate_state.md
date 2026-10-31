---
title: "aupdate_state"
description: "Asynchronously update the state of the graph with the given values, as if they came from node as_node. If as_node is not provided, it will be set to the last node that updated the state, if not..."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/aupdate_state"
category: "reference"
tags: [reference, langgraph, pregel, main, aupdate_state]
---

# aupdate_state

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/aupdate_state)

Asynchronously update the state of the graph with the given values, as if they came from
node `as_node`. If `as_node` is not provided, it will be set to the last node
that updated the state, if not ambiguous.

## Signature

```python
aupdate_state(
    self,
    config: RunnableConfig,
    values: dict[str, Any] | Any,
    as_node: str | None = None,
    task_id: str | None = None,
) -> RunnableConfig
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/pregel/main.py#L2626)
