---
title: "tool_calls"
description: "Tool-execution projection (the tools channel)."
source: "https://reference.langchain.com/python/langgraph/pregel/_remote_run_stream/_AsyncRemoteGraphRunStream/tool_calls"
category: "reference"
tags: [reference, langgraph, pregel, remote_run_stream, asyncremotegraphrunstream, tool_calls]
---

# tool_calls

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_remote_run_stream/_AsyncRemoteGraphRunStream/tool_calls)

Tool-execution projection (the `tools` channel).

These are tool *execution* events (started / output / finished),
distinct from the tool-call *inputs* carried inside `messages`.

## Signature

```python
tool_calls: Any
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/_remote_run_stream.py#L336)
