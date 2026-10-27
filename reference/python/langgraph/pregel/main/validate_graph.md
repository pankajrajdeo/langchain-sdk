---
title: "validate_graph"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/main/validate_graph"
category: "reference"
tags: [reference, langgraph, pregel, main, validate_graph]
---

# validate_graph

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_validate/validate_graph)

## Signature

```python
validate_graph(
    nodes: Mapping[str, PregelNode],
    channels: dict[str, BaseChannel],
    managed: ManagedValueMapping,
    input_channels: str | Sequence[str],
    output_channels: str | Sequence[str],
    stream_channels: str | Sequence[str] | None,
    interrupt_after_nodes: All | Sequence[str],
    interrupt_before_nodes: All | Sequence[str],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/_validate.py#L13)
