---
title: "process_inputs"
description: "Optional callable to transform the node's input before it is recorded on the node's trace run. Can be used to omit or summarize large payloads (e.g. message history). Not intended to affect the value..."
source: "https://reference.langchain.com/python/langgraph/types/TracePolicy/process_inputs"
category: "reference"
tags: [reference, langgraph, types, tracepolicy, process_inputs]
---

# process_inputs

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TracePolicy/process_inputs)

Optional callable to transform the node's input before it is recorded on the
node's trace run. Can be used to omit or summarize large payloads
(e.g. message history). Not intended to affect the value passed to the node; avoid
mutating arguments in place.

## Signature

```python
process_inputs: Callable[[Any], Any] | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/types.py#L557)
