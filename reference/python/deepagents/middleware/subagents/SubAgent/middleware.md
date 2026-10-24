---
title: "middleware"
description: "Additional middleware for custom behavior, logging, or rate limiting."
source: "https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/middleware"
category: "reference"
tags: [reference, deepagents, middleware, subagents, subagent]
---

# middleware

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/subagents/SubAgent/middleware)

Additional middleware for custom behavior, logging, or rate limiting.

Under `mode="fork"`, inherits the parent's custom middleware list. Entries
in this list replace inherited entries with the same `.name`; entries with
other names are added.

Avoid middleware that rewrites the inherited system-prompt prefix in the
fork's model request or changes tool definitions unless you accept reduced
shared prompt-cache reuse and potentially higher model costs. This is
distinct from `SubAgent.system_prompt`, which appends instructions to the
inherited prompt. A `wrap_model_call` hook receives that prompt through
`request.system_message`. For example, this prepends text before the inherited
prefix in the fork's request, preventing reuse of that prefix:

```python
from langchain_core.messages import SystemMessage

rewritten = SystemMessage(content=[
    {"type": "text", "text": "You are a security auditor.\n"},
    *request.system_message.content_blocks,
])
return handler(request.override(system_message=rewritten))
```

To restrict filesystem tools, include a `FilesystemMiddleware(tools=...)`
instance here to replace the subagent's default filesystem middleware.

## Signature

```python
middleware: NotRequired[list[AgentMiddleware]]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/subagents.py#L124)
