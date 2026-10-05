---
title: "message"
description: "The human-provided reason for rejecting the action."
source: "https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/RejectDecision/message"
category: "reference"
tags: [reference, langchain, agents, middleware, human_in_the_loop, rejectdecision, message]
---

# message

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/human_in_the_loop/RejectDecision/message)

The human-provided reason for rejecting the action.

The reason is framed as a user rejection when sent to the model. If omitted,
the model is told that the tool was not executed and should not retry the same
tool call unless the user asks for it.

## Signature

```python
message: NotRequired[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/middleware/human_in_the_loop.py#L117)
