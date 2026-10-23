---
title: "RunModule"
description: "Command dispatcher for run.start."
source: "https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule"
category: "reference"
tags: [reference, langgraph-sdk, async, stream, runmodule]
---

# RunModule

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule)

Command dispatcher for `run.start`.

Bound to one `AsyncThreadStream`; accesses its transport and id allocator.

## Signature

```python
RunModule(
    self,
    owner: AsyncThreadStream,
)
```

## Constructors

```python
__init__(
    self,
    owner: AsyncThreadStream,
) -> None
```

| Name | Type |
|------|------|
| `owner` | `AsyncThreadStream` |

## Methods

- [`start()`](https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule/start)
- [`respond()`](https://reference.langchain.com/python/langgraph-sdk/_async/stream/RunModule/respond)

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/sdk-py/langgraph_sdk/_async/stream.py#L169)
