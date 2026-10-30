---
title: "Managed Deep Agents v0.10: Browser use and asynchronous subagents"
description: "Managed Deep Agents v0.10 adds browser use, so agents can work on sites with no API and hand you the window to sign in, and async subagents for background work."
source: "https://www.langchain.com/blog/managed-deep-agents-browser-use-and-asynchronous-subagents"
category: "blog"
published: "2026-10-29T16:54:00.000Z"
author: "LangChain Accounts"
tags: [blog, managed-deep-agents-browser-use-and-asynchronous-subagents]
---

# Managed Deep Agents v0.10: Browser use and asynchronous subagents

- **Browser use:** Your agent can book travel or file a claim on sites that have no API. When a site asks you to sign in, the agent hands you the browser window, so your password stays out of the model's messages and traces.
- **Async subagents:** A long job can go to a subagent that runs in the background while your agent keeps talking with you. You can ask the agent to check on the job or change its course, and the result comes back to the conversation when the subagent finishes.
- **Thread origins and stopping runs:** Replies go back to the Slack thread a request started in, including replies from a scheduled run or from a subagent that finished later. A Stop button in the thread cancels its runs.
