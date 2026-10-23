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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/_io.py#L56)
