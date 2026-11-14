---
title: "get_state_history"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/get_state_history"
category: "reference"
tags: [reference, langgraph, pregel, protocol, pregelprotocol, get_state_history]
---

# get_state_history

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/get_state_history)

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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/pregel/protocol.py#L57)
