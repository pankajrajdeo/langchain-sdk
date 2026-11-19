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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/_algo.py#L158)
