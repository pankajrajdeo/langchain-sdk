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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/callbacks/file.py#L252)
