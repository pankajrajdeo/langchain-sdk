---
title: "map_output_values"
description: "Map pending writes (a sequence of tuples (channel, value)) to output chunk."
source: "https://reference.langchain.com/python/langgraph/pregel/_io/map_output_values"
category: "reference"
tags: [reference, langgraph, pregel, io, map_output_values]
---

# map_output_values

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_io/map_output_values)

Map pending writes (a sequence of tuples (channel, value)) to output chunk.

## Signature

```python
map_output_values(
    output_channels: str | Sequence[str],
    pending_writes: Literal[True] | Sequence[tuple[str, Any]],
    channels: Mapping[str, BaseChannel],
) -> Iterator[dict[str, Any] | Any]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/_io.py#L100)
