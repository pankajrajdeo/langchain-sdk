---
title: "async_subagents"
description: "Middleware for async subagents running on remote Agent Protocol servers."
source: "https://reference.langchain.com/python/deepagents/middleware/async_subagents"
category: "reference"
tags: [reference, deepagents, middleware, async_subagents]
---

# async_subagents

> **Module** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/async_subagents)

Middleware for async subagents running on remote Agent Protocol servers.

Async subagents use the LangGraph SDK to launch background runs on remote
[Agent Protocol](https://github.com/langchain-ai/agent-protocol) servers.
Unlike synchronous subagents (which block until completion), async subagents
return a task ID immediately, allowing the main agent to monitor progress and
send updates while the subagent works.

Compatible with LangGraph Platform (managed) and self-hosted servers.

## Properties

- `NUM_CHARS_PER_TOKEN`
- `SUMMARIZATION_EVENT_KEY`
- `logger`
- `ASYNC_TASK_TOOL_DESCRIPTION`

## Methods

- [`append_to_system_message()`](https://reference.langchain.com/python/deepagents/middleware/async_subagents/append_to_system_message)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/async_subagents.py)
