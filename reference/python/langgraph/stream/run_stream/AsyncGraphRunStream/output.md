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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/stream/run_stream.py#L583)
