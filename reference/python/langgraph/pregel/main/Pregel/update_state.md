---
title: "update_state"
description: "Update the state of the graph with the given values, as if they came from node as_node. If as_node is not provided, it will be set to the last node that updated the state, if not ambiguous."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/update_state"
category: "reference"
tags: [reference, langgraph, pregel, main, update_state]
---

# update_state

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/update_state)

Update the state of the graph with the given values, as if they came from
node `as_node`. If `as_node` is not provided, it will be set to the last node
that updated the state, if not ambiguous.

## Signature

```python
update_state(
    self,
    config: RunnableConfig,
    values: dict[str, Any] | Any | None,
    as_node: str | None = None,
    task_id: str | None = None,
) -> RunnableConfig
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/main.py#L2515)
