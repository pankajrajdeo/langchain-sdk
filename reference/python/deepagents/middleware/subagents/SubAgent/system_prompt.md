---
title: "system_prompt"
description: "Instructions for the subagent. Uses an empty prompt when omitted."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/system_prompt"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagent, system_prompt]
---

# system_prompt

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/system_prompt)

Instructions for the subagent. Uses an empty prompt when omitted.

Under `mode="fork"` the fork keeps the parent's system prompt unchanged so it
can reuse the parent's cached prompt prefix; these instructions are delivered
with the task message after the inherited conversation instead.

## Signature

```python
system_prompt: NotRequired[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/middleware/subagents.py#L250)
