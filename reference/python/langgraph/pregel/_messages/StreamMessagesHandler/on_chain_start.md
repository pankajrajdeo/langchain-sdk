---
title: "on_chain_start"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandler/on_chain_start"
category: "reference"
tags: [reference, langgraph, pregel, messages, streammessageshandler, on_chain_start]
---

# on_chain_start

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_messages/StreamMessagesHandler/on_chain_start)

## Signature

```python
on_chain_start(
    self,
    serialized: dict[str, Any],
    inputs: dict[str, Any],
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    kwargs: Any = {},
) -> Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/pregel/_messages.py#L215)
