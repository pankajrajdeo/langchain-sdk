---
title: "map_command"
description: "Map input chunk to a sequence of pending writes in the form (channel, value)."
source: "https://reference.langchain.com/python/langgraph/pregel/_io/map_command"
category: "reference"
tags: [reference, langgraph, pregel, io, map_command]
---

# map_command

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_io/map_command)

Map input chunk to a sequence of pending writes in the form (channel, value).

## Signature

```python
map_command(
    cmd: Command,
) -> Iterator[tuple[str, str, Any]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/pregel/_io.py#L56)
