---
title: "log"
description: "Additional information to log about the action."
source: "https://reference.langchain.com/python/langchain-core/agents/AgentAction/log"
category: "reference"
tags: [reference, langchain-core, agents, agentaction, log]
---

# log

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/agents/AgentAction/log)

Additional information to log about the action.

This log can be used in a few ways. First, it can be used to audit what exactly the
LLM predicted to lead to this `(tool, tool_input)`.

Second, it can be used in future iterations to show the LLMs prior thoughts. This is
useful when `(tool, tool_input)` does not contain full information about the LLM
prediction (for example, any `thought` before the tool/tool_input).

## Signature

```python
log: str
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/agents.py#L57)
