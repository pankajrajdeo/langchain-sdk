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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_io.py#L56)
