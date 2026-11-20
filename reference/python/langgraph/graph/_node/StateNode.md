---
title: "StateNode"
description: "Type Alias in langgraph"
source: "https://reference.langchain.com/python/langgraph/graph/_node/StateNode"
category: "reference"
tags: [reference, langgraph, graph, node, statenode]
---

# StateNode

> **Type Alias** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/graph/_node/StateNode)

## Signature

```python
StateNode: TypeAlias = _Node[NodeInputT] | _NodeWithConfig[NodeInputT] | _NodeWithWriter[NodeInputT] | _NodeWithStore[NodeInputT] | _NodeWithWriterStore[NodeInputT] | _NodeWithConfigWriter[NodeInputT] | _NodeWithConfigStore[NodeInputT] | _NodeWithConfigWriterStore[NodeInputT] | _NodeWithRuntime[NodeInputT, ContextT] | Runnable[NodeInputT, Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/58a6e1cc5b7dfc3619fc6e7e7573b040d554649b/libs/langgraph/langgraph/graph/_node.py#L76)
