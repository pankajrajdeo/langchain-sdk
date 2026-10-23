---
title: "Context Engineering: How Deep Agents Remember"
description: "Long-running agents degrade as context piles up. Learn how offloading, summarization, skills, subagents, and memory keep your agent&#39;s context window focused."
source: "https://www.langchain.com/blog/context-engineering-deep-agents-remember"
category: "blog"
published: "2026-10-14T17:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, context-engineering-deep-agents-remember]
---

# Context Engineering: How Deep Agents Remember

- "Context rot" happens as long-running agents build up more context than the model can hold, resulting in accuracy drops.
- Deep Agents, LangChain's open source agent harness, uses five techniques to move context *out* of the active window (without deleting it) to prevent context rot.
- An agent's memory in Deep Agents is stored as plain files in storage you control, so you can switch models or providers while keeping everything it has learned.
