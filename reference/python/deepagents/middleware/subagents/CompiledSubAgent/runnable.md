---
title: "runnable"
description: "A custom agent implementation."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/CompiledSubAgent/runnable"
category: "reference"
tags: [reference, deepagents, middleware, subagents, compiledsubagent, runnable]
---

# runnable

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/CompiledSubAgent/runnable)

A custom agent implementation.

Create a custom agent using either:

1. LangChain's [`create_agent()`](../../../../../../langchain/quickstart.md)
2. A custom graph using [`langgraph`](../../../../../../langgraph/quickstart.md)

If you're creating a custom graph, make sure the state schema includes
a 'messages' key. This is required for the subagent to communicate
results back to the main agent.

## Signature

```python
runnable: Runnable
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/subagents.py#L296)
