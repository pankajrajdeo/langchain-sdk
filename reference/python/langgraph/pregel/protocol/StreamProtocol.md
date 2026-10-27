---
title: "StreamProtocol"
description: "- modes"
source: "https://reference.langchain.com/python/langgraph/pregel/protocol/StreamProtocol"
category: "reference"
tags: [reference, langgraph, pregel, protocol, streamprotocol]
---

# StreamProtocol

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/protocol/StreamProtocol)

## Signature

```python
StreamProtocol(
    self,
    __call__: Callable[[StreamChunk], None],
    modes: set[StreamMode],
)
```

## Constructors

```python
__init__(
    self,
    __call__: Callable[[StreamChunk], None],
    modes: set[StreamMode],
) -> None
```

| Name | Type |
|------|------|
| `__call__` | `Callable[[StreamChunk], None]` |
| `modes` | `set[StreamMode]` |

## Properties

- `modes`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/protocol.py#L275)
