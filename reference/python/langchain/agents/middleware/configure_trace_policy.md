---
title: "configure_trace_policy"
description: "Set the process-wide default TracePolicy for agent middleware hook spans."
source: "https://reference.langchain.com/python/langchain/agents/middleware/configure_trace_policy"
category: "reference"
tags: [reference, langchain, agents, middleware, configure_trace_policy]
---

# configure_trace_policy

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_trace_policy/configure_trace_policy)

Set the process-wide default `TracePolicy` for agent middleware hook spans.

Call once at startup. A middleware's own `trace_policy` overrides this wholesale
(no field-level merge). Pass `None` to clear the default.

## Signature

```python
configure_trace_policy(
    policy: TracePolicy | None,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/_trace_policy.py#L22)
