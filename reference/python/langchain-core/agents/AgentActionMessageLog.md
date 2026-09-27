---
title: "AgentActionMessageLog"
description: "Representation of an action to be executed by an agent."
source: "https://reference.langchain.com/python/langchain-core/agents/AgentActionMessageLog"
category: "reference"
tags: [reference, langchain-core, agents, agentactionmessagelog]
---

# AgentActionMessageLog

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/agents/AgentActionMessageLog)

Representation of an action to be executed by an agent.

This is similar to `AgentAction`, but includes a message log consisting of
chat messages.

This is useful when working with `ChatModels`, and is used to reconstruct
conversation history from the agent's perspective.

## Signature

```python
AgentActionMessageLog(
    self,
    tool: str,
    tool_input: str | dict[Any, Any],
    log: str,
    **kwargs: Any = {},
)
```

## Extends

- `AgentAction`

## Properties

- `message_log`
- `type`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/agents.py#L107)
