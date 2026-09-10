---
title: "log"
description: "Additional information to log about the return value."
source: "https://reference.langchain.com/python/langchain-core/agents/AgentFinish/log"
category: "reference"
tags: [reference, langchain-core, agents, agentfinish, log]
---

# log

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/agents/AgentFinish/log)

Additional information to log about the return value.

This is used to pass along the full LLM prediction, not just the parsed out
return value.

For example, if the full LLM prediction was `Final Answer: 2` you may want to just
return `2` as a return value, but pass along the full string as a `log` (for
debugging or observability purposes).

## Signature

```python
log: str
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/agents.py#L157)
