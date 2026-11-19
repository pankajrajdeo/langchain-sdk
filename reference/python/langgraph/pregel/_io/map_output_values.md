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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/_io.py#L100)
