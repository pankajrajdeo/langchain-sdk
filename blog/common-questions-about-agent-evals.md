---
title: "The Most Common Questions About Agent Evals, Answered"
description: "Where to start with agent evals, offline vs online evals, evaluator types, LLM judges, benchmarks with Harbor, multi-turn evals, and keeping costs down."
source: "https://www.langchain.com/blog/common-questions-about-agent-evals"
category: "blog"
published: "2026-10-15T19:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, common-questions-about-agent-evals]
---

# The Most Common Questions About Agent Evals, Answered

- **Evals score your agent's runs so you can check that it behaves the way you expect.** To get started, pick one behavior, build a small dataset from real traces, and run a baseline. Use offline evals before you ship and online evals in production, and turn new failures into dataset examples.
- **Use code evaluators where you can, LLM judges where you can't, and human review to check both.** For agents that take many steps, evaluate full threads, trajectories, and final state.
- **Benchmarks like Terminal-Bench are offline evals with longer tasks and their own environments.** Harbor runs them and logs the results to LangSmith experiments.
