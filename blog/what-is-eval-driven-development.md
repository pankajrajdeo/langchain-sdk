---
title: "What Is Eval-Driven Development? How to Improve AI Agents"
description: "Eval-driven development helps you build AI agents against a consistent set of metrics. Define good behavior, write the eval first, then compare experiments."
source: "https://www.langchain.com/blog/what-is-eval-driven-development"
category: "blog"
published: "2026-11-09T19:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, what-is-eval-driven-development]
---

# What Is Eval-Driven Development? How to Improve AI Agents

- **Eval-driven development (EDD) involves building an agent while measuring performance against a consistent set of metrics and hill climbing toward an eval.**
- **The first step of EDD is to create a short spec of what good looks like for your desired behavior.** Include what the agent shouldn't do and what has to keep working.
- **As you iterate, judge a change you make to the agent by comparing experiments.** A change that fixes one case may break another.
- **Keep evals running in CI and in production, and turn the failures you find into new dataset examples.**
