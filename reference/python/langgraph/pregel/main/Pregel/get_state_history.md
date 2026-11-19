---
title: "get_state_history"
description: "Get the history of the state of the graph."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/get_state_history"
category: "reference"
tags: [reference, langgraph, pregel, main, get_state_history]
---

# get_state_history

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/get_state_history)

Get the history of the state of the graph.

## Signature

```python
get_state_history(
    self,
    config: RunnableConfig,
    *,
    filter: dict[str, Any] | None = None,
    before: RunnableConfig | None = None,
    limit: int | None = None,
) -> Iterator[StateSnapshot]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/main.py#L1529)
