---
title: "interrupted"
description: "Whether the remote run is currently paused at an interrupt."
source: "https://reference.langchain.com/python/langgraph/pregel/_remote_run_stream/_RemoteGraphRunStream/interrupted"
category: "reference"
tags: [reference, langgraph, pregel, remote_run_stream, remotegraphrunstream, interrupted]
---

# interrupted

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_remote_run_stream/_RemoteGraphRunStream/interrupted)

Whether the remote run is currently paused at an interrupt.

Reads the SDK's current value without blocking. This differs from
local `GraphRunStream.interrupted`, which drives the run to terminal
before returning the flag. Sync callers needing a wait-for-interrupt
pattern should switch to the async API and drain a projection.

## Signature

```python
interrupted: bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/_remote_run_stream.py#L177)
