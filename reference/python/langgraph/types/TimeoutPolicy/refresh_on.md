---
title: "refresh_on"
description: "Which signals refresh idle_timeout."
source: "https://reference.langchain.com/python/langgraph/types/TimeoutPolicy/refresh_on"
category: "reference"
tags: [reference, langgraph, types, timeoutpolicy, refresh_on]
---

# refresh_on

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TimeoutPolicy/refresh_on)

Which signals refresh `idle_timeout`.

`"auto"` refreshes on standard graph progress signals and explicit heartbeats.
`"heartbeat"` refreshes only on explicit `runtime.heartbeat()` calls.

## Signature

```python
refresh_on: Literal['auto', 'heartbeat'] = 'auto'
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/langgraph/langgraph/types.py#L485)
