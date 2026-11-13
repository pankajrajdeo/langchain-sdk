---
title: "aget_state_history"
description: "Asynchronously get the history of the state of the graph."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/aget_state_history"
category: "reference"
tags: [reference, langgraph, pregel, main, aget_state_history]
---

# aget_state_history

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/aget_state_history)

Asynchronously get the history of the state of the graph.

## Signature

```python
aget_state_history(
    self,
    config: RunnableConfig,
    *,
    filter: dict[str, Any] | None = None,
    before: RunnableConfig | None = None,
    limit: int | None = None,
) -> AsyncIterator[StateSnapshot]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/pregel/main.py#L1569)
