---
title: "created_at_index"
description: "Number of state messages when the summary was created."
source: "https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationEvent/created_at_index"
category: "reference"
tags: [reference, deepagents, middleware, summarization, summarizationevent, created_at_index]
---

# created_at_index

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/summarization/SummarizationEvent/created_at_index)

Number of state messages when the summary was created.

Messages from `cutoff_index` up to this index were kept verbatim from before
the summary. Claude binds each reasoning block to the conversation before it
and can reject a request once that conversation changes, so their reasoning
blocks are left out of the messages the model sees. Absent on events created
before this field existed.

## Signature

```python
created_at_index: NotRequired[int]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/summarization.py#L161)
