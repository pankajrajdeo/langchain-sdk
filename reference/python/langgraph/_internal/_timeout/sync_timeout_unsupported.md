---
title: "sync_timeout_unsupported"
description: "Build the canonical error for using timeout with a sync target."
source: "https://reference.langchain.com/python/langgraph/_internal/_timeout/sync_timeout_unsupported"
category: "reference"
tags: [reference, langgraph, internal, timeout, sync_timeout_unsupported]
---

# sync_timeout_unsupported

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_timeout/sync_timeout_unsupported)

Build the canonical error for using `timeout` with a sync target.

## Signature

```python
sync_timeout_unsupported(
    name: str,
    *,
    kind: Literal['Node', 'Task'] = 'Node',
) -> ValueError
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/_internal/_timeout.py#L21)
