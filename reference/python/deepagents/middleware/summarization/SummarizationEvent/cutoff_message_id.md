---
title: "cutoff_message_id"
description: "Id of the message at cutoff_index; stays correct when earlier messages are removed."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationEvent/cutoff_message_id"
category: "reference"
tags: [reference, deepagents, middleware, summarization, summarizationevent, cutoff_message_id]
---

# cutoff_message_id

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationEvent/cutoff_message_id)

Id of the message at `cutoff_index`; stays correct when earlier messages are removed.

`None` if that message has no id. Absent on events created before this field existed.

## Signature

```python
cutoff_message_id: NotRequired[str | None]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/middleware/summarization.py#L164)
