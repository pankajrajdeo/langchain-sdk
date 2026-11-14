---
title: "invoke"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/invoke"
category: "reference"
tags: [reference, langgraph, pregel, protocol, pregelprotocol, invoke]
---

# invoke

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/invoke)

## Signature

```python
invoke(
    self,
    input: InputT | Command | None,
    config: RunnableConfig | None = None,
    *,
    context: ContextT | None = None,
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    version: Literal['v1', 'v2'] = 'v1',
) -> dict[str, Any] | Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/08a2016953789a4f579b4d36bd1967941ec62012/libs/langgraph/langgraph/pregel/protocol.py#L221)
