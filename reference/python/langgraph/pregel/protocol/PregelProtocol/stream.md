---
title: "stream"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/stream"
category: "reference"
tags: [reference, langgraph, pregel, protocol, pregelprotocol, stream]
---

# stream

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/protocol/PregelProtocol/stream)

## Signature

```python
stream(
    self,
    input: InputT | Command | None,
    config: RunnableConfig | None = None,
    *,
    context: ContextT | None = None,
    stream_mode: StreamMode | list[StreamMode] | None = None,
    interrupt_before: All | Sequence[str] | None = None,
    interrupt_after: All | Sequence[str] | None = None,
    subgraphs: bool = False,
    version: Literal['v1', 'v2'] = 'v1',
) -> Iterator[dict[str, Any] | Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/protocol.py#L137)
