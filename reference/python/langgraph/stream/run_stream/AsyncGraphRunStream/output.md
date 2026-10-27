---
title: "output"
description: "Drive the run to completion and return the final state."
source: "https://reference.langchain.com/python/langgraph/stream/run_stream/AsyncGraphRunStream/output"
category: "reference"
tags: [reference, langgraph, stream, run_stream, asyncgraphrunstream, output]
---

# output

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/stream/run_stream/AsyncGraphRunStream/output)

Drive the run to completion and return the final state.

Methods (not properties) on the async lane so `run.output`
without `await` raises at type-check time instead of silently
yielding a coroutine object.

## Signature

```python
output(
    self,
) -> dict[str, Any] | None
```

## Description

**Example:**

```python
output = await run.output()
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/stream/run_stream.py#L583)
