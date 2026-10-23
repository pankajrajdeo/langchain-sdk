---
title: "Revamping Skills in Deep Agents"
description: "Deep Agents now lets you bind tools to skills, pin skills at runtime, and reload skills mid-thread, so agents with expansive skill repositories stay context-efficient and effective."
source: "https://www.langchain.com/blog/revamping-skills-in-deep-agents"
category: "blog"
published: "2026-10-07T19:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, revamping-skills-in-deep-agents]
---

# Revamping Skills in Deep Agents

- **You can now bind tools to skills.** Tool schemas stay out of context until the agent reads the skill they're bound to, and on models that accept new tools mid-conversation, adding them keeps the prompt cache intact.
- **Apps can pin skills at runtime**, so the instructions are in context before the first model call, with no `read_file` round trips.
- **Skills can reload mid-thread**, so a long-running agent picks up added, edited, or deleted skills without starting a new thread.
