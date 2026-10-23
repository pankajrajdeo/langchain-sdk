---
title: "Building Long-Running Agents with ScaleDown and Deep Agents"
description: "Use ScaleDown&#39;s constrained decoding models with LangChain and Deep Agents to summarize history, compress tool results, and extract data faster and cheaper."
source: "https://www.langchain.com/blog/building-long-running-agents-with-scaledown-and-deep-agents"
category: "blog"
published: "2026-10-13T11:55:00.000Z"
author: "LangChain Accounts"
tags: [blog, building-long-running-agents-with-scaledown-and-deep-agents]
---

# Building Long-Running Agents with ScaleDown and Deep Agents

- Building long-running agents takes constant context management, and making those decisions with a frontier LLM is slow and expensive. ScaleDown’s constrained decoding models (CDMs) make them faster and cheaper.
- `langchain-scaledown` makes it easy to use ScaleDown models in your agent, and ships with middleware for summarization, tool result compression, and extraction.
- ScaleDown is now supported in the LangSmith LLM Gateway, so its calls are traced and count toward your spend and rate limits.
