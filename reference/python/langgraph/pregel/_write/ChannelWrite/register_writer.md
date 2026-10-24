---
title: "register_writer"
description: "Used to mark a runnable as a writer, so that it can be detected by is_writer. Instances of ChannelWrite are automatically marked as writers. Optionally, a list of declared writes can be passed for..."
source: "https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/register_writer"
category: "reference"
tags: [reference, langgraph, pregel, write, channelwrite, register_writer]
---

# register_writer

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_write/ChannelWrite/register_writer)

Used to mark a runnable as a writer, so that it can be detected by is_writer.
Instances of ChannelWrite are automatically marked as writers.
Optionally, a list of declared writes can be passed for static analysis.

## Signature

```python
register_writer(
    runnable: R,
    static: Sequence[tuple[ChannelWriteEntry | Send, str | None]] | None = None,
) -> R
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_write.py#L158)
