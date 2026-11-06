---
title: "Agents Are Going Async"
description: "Async subagents let an agent stay responsive while background workers run long tasks. How the orchestrator, notifications and approvals work in Deep Agents."
source: "https://www.langchain.com/blog/agents-are-going-async"
category: "blog"
published: "2026-11-05T20:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, agents-are-going-async]
---

# Agents Are Going Async

- As agents take on bigger goals, they need to stay responsive to the user while making progress on many long tasks at once.
- Async subagents split an agent into an orchestrator that stays available to the user and subagents that run tasks in the background and report back to the orchestrator upon completion.
- Background work is becoming the norm for agent infrastructure, from coding agents like Claude Code to personal agents like OpenAI's dots.
