---
title: "transformer_requires_async"
description: "Return True if the transformer needs a running event loop."
source: "https://reference.langchain.com/python/langgraph/stream/_types/transformer_requires_async"
category: "reference"
tags: [reference, langgraph, stream, types, transformer_requires_async]
---

# transformer_requires_async

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/_types/transformer_requires_async)

Return True if the transformer needs a running event loop.

A transformer requires async if it explicitly opts in
(`requires_async = True`) or overrides any of the async-lane methods
(`aprocess`, `afinalize`, `afail`) without also declaring that it
supports the sync lane.

## Signature

```python
transformer_requires_async(
    transformer: StreamTransformer,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `transformer` | `StreamTransformer` | Yes | The transformer to inspect. |

## Returns

`bool`

True if the transformer cannot run under sync `stream()`.

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/stream/_types.py#L308)
