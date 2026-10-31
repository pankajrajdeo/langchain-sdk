---
title: "graph_namespace"
description: "Namespace of the graph a task runs in, from the task's run metadata."
source: "https://reference.langchain.com/python/langgraph/pregel/_messages/graph_namespace"
category: "reference"
tags: [reference, langgraph, pregel, messages, graph_namespace]
---

# graph_namespace

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_messages/graph_namespace)

Namespace of the graph a task runs in, from the task's run metadata.

Drops the task's own segment, plus one per enclosing `@task` call: a call
runs in its caller's graph but nests its segment under the caller's. A
call's `langgraph_path` is `(PUSH, <caller's path>, <index>, True)`, while
a `Send` task's ends in `False`.

## Signature

```python
graph_namespace(
    metadata: Mapping[str, Any],
) -> tuple[str, ...]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/pregel/_messages.py#L58)
