---
title: "on_agent_finish"
description: "Handle agent finish by writing the finish log."
source: "https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_agent_finish"
category: "reference"
tags: [reference, langchain-core, callbacks, file, filecallbackhandler, on_agent_finish]
---

# on_agent_finish

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/file/FileCallbackHandler/on_agent_finish)

Handle agent finish by writing the finish log.

## Signature

```python
on_agent_finish(
    self,
    finish: AgentFinish,
    color: str | None = None,
    **kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `finish` | `AgentFinish` | Yes | The agent finish object containing the log to write. |
| `color` | `str \| None` | No | Color override for this specific output.  If `None`, uses `self.color`. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/file.py#L253)
