---
title: "on_agent_action"
description: "Run when agent action is received."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainRun/on_agent_action"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanagerforchainrun, on_agent_action]
---

# on_agent_action

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManagerForChainRun/on_agent_action)

Run when agent action is received.

## Signature

```python
on_agent_action(
    self,
    action: AgentAction,
    kwargs: Any = {},
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `action` | `AgentAction` | Yes | The agent action. |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/callbacks/manager.py#L988)
