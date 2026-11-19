---
title: "GraphRecursionError"
description: "Raised when the graph has exhausted the maximum number of steps."
source: "https://reference.langchain.com/python/langgraph/errors/GraphRecursionError"
category: "reference"
tags: [reference, langgraph, errors, graphrecursionerror]
---

# GraphRecursionError

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/errors/GraphRecursionError)

Raised when the graph has exhausted the maximum number of steps.

This prevents infinite loops. To increase the maximum number of steps,
run your graph with a config specifying a higher `recursion_limit`.

Troubleshooting guides:

- [`GRAPH_RECURSION_LIMIT`](../../../../langgraph/GRAPH_RECURSION_LIMIT.md)

Examples:

    graph = builder.compile()
    graph.invoke(
        {"messages": [("user", "Hello, world!")]},
        # The config is the second positional argument
        {"recursion_limit": 1000},
    )

## Signature

```python
GraphRecursionError()
```

## Extends

- `RecursionError`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/errors.py#L69)
