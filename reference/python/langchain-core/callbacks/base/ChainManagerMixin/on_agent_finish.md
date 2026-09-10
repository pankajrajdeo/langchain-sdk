---
title: "on_agent_finish"
description: "Run on the agent end."
source: "https://reference.langchain.com/python/langchain-core/callbacks/base/ChainManagerMixin/on_agent_finish"
category: "reference"
tags: [reference, langchain-core, callbacks, base, chainmanagermixin, on_agent_finish]
---

# on_agent_finish

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/base/ChainManagerMixin/on_agent_finish)

Run on the agent end.

## Signature

```python
on_agent_finish(
    self,
    finish: AgentFinish,
    *,
    run_id: UUID,
    parent_run_id: UUID | None = None,
    **kwargs: Any = {},
) -> Any
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `finish` | `AgentFinish` | Yes | The agent finish. |
| `run_id` | `UUID` | Yes | The ID of the current run. |
| `parent_run_id` | `UUID \| None` | No | The ID of the parent run. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/callbacks/base.py#L223)
