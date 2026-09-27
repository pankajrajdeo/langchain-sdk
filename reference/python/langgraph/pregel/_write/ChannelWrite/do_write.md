---
title: "do_write"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/do_write"
category: "reference"
tags: [reference, langgraph, pregel, write, channelwrite, do_write]
---

# do_write

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/do_write)

## Signature

```python
do_write(
    config: RunnableConfig,
    writes: Sequence[ChannelWriteEntry | ChannelWriteTupleEntry | Send],
    allow_passthrough: bool = True,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_write.py#L105)
