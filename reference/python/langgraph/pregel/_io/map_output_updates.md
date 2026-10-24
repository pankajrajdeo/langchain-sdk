---
title: "map_output_updates"
description: "Map pending writes (a sequence of tuples (channel, value)) to output chunk."
source: "https://reference.langchain.com/python/langgraph/pregel/_io/map_output_updates"
category: "reference"
tags: [reference, langgraph, pregel, io, map_output_updates]
---

# map_output_updates

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_io/map_output_updates)

Map pending writes (a sequence of tuples (channel, value)) to output chunk.

## Signature

```python
map_output_updates(
    output_channels: str | Sequence[str],
    tasks: list[tuple[PregelExecutableTask, Sequence[tuple[str, Any]]]],
    cached: bool = False,
) -> Iterator[dict[str, Any | dict[str, Any]]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_io.py#L118)
