---
title: "checkpoint_superseded"
description: "Whether the thread has moved past saved, the checkpoint config addressed."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/checkpoint_superseded"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, checkpoint_superseded]
---

# checkpoint_superseded

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/checkpoint_superseded)

Whether the thread has moved past `saved`, the checkpoint `config` addressed.

A checkpoint with a child is never the latest put, so this misses none. A
leaf of an abandoned branch counts as well; telling it apart would mean
listing the thread to look for children, which the saver can't do cheaply.

## Signature

```python
checkpoint_superseded(
    saver: BaseCheckpointSaver,
    config: RunnableConfig,
    saved: CheckpointTuple,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_checkpoint.py#L174)
