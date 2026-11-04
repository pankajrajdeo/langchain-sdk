---
title: "How We Optimized Browser Use for Deep Agents"
description: "We compared seven browser toolsets for Deep Agents, picked Stagehand from Browserbase, and tuned it with LangSmith traces and evals. Here&#39;s what we learned."
source: "https://www.langchain.com/blog/how-we-optimized-browser-use-for-deep-agents"
category: "blog"
published: "2026-11-03T16:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, how-we-optimized-browser-use-for-deep-agents]
---

# How We Optimized Browser Use for Deep Agents

- Browser use is an important capability for agents doing autonomous work, letting them act on sites built for people.
- The tools an agent uses to drive the browser have a huge impact on its cost and trajectory, and Stagehand's are built for agents.
- Optimizing tools is an iterative process: trace the agent's behavior to find where it's inefficient, update the harness, and test every change with evals before keeping it.
