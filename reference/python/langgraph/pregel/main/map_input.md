---
title: "map_input"
description: "Map input chunk to a sequence of pending writes in the form (channel, value)."
source: "https://reference.langchain.com/python/langgraph/pregel/main/map_input"
category: "reference"
tags: [reference, langgraph, pregel, main, map_input]
---

# map_input

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_io/map_input)

Map input chunk to a sequence of pending writes in the form (channel, value).

## Signature

```python
map_input(
    input_channels: str | Sequence[str],
    chunk: dict[str, Any] | Any | None,
) -> Iterator[tuple[str, Any]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/_io.py#L81)
