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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/protocol.py#L275)
