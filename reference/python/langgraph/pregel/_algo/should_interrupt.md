---
title: "should_interrupt"
description: "Check if the graph should be interrupted based on current state."
source: "https://reference.langchain.com/python/langgraph/pregel/_algo/should_interrupt"
category: "reference"
tags: [reference, langgraph, pregel, algo, should_interrupt]
---

# should_interrupt

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_algo/should_interrupt)

Check if the graph should be interrupted based on current state.

## Signature

```python
should_interrupt(
    checkpoint: Checkpoint,
    interrupt_nodes: All | Sequence[str],
    tasks: Iterable[PregelExecutableTask],
) -> list[PregelExecutableTask]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_algo.py#L156)
