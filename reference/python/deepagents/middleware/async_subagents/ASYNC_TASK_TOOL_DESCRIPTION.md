---
title: "ASYNC_TASK_TOOL_DESCRIPTION"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents/ASYNC_TASK_TOOL_DESCRIPTION"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents, async_task_tool_description]
---

# ASYNC_TASK_TOOL_DESCRIPTION

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents/ASYNC_TASK_TOOL_DESCRIPTION)

## Signature

```python
ASYNC_TASK_TOOL_DESCRIPTION = "Start an async subagent on a remote server. The subagent runs in the background and returns a task ID immediately.\n\nAvailable async agent types:\n{available_agents}\n\n## Usage notes:\n1. This tool launches a background task and returns immediately with a task ID for internal coordination. Briefly describe the delegated work and whether you are continuing other work or waiting for results. Omit task IDs from user-facing replies unless explicitly requested or necessary for actionable troubleshooting. Do NOT immediately check status.\n2. You'll usually be told when a task finishes, fails or needs input, so don't check just to see if it's done; use `check_async_task` when the user asks or a notification says to.\n3. Use `update_async_task` to send new instructions to a running task.\n4. Multiple async subagents can run concurrently — launch several and let them run in the background.\n5. The subagent runs on a remote server, so it has its own tools and capabilities.\n6. A task with status `waiting` is waiting for a human (an approval or an answer). The user answers it directly; you can't answer or approve it for them. Keep working, and tell the user it's waiting if they ask."
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/async_subagents.py#L290)
