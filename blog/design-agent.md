---
title: "How We Built Our Design Agent"
description: "How LangChain built Content Studio, an open-source design agent in Slack that makes on-brand videos, graphics and decks, and the harness that powers it."
source: "https://www.langchain.com/blog/design-agent"
category: "blog"
published: "2026-10-27T16:45:00.000Z"
author: "LangChain Accounts"
tags: [blog, design-agent]
---

# How We Built Our Design Agent

- **Taste comes from context.** Models already write good code, but they need your designers’ principles, guardrails against AI slop, and the reasoning behind feedback to make work that looks like yours.
- **Give the agent a designer’s computer.** Every Slack thread gets its own sandbox where the agent keeps the project between turns, works across a video engine, image tools, and a shared canvas, and inspects its own renders.
- **Delete rules when the model improves.** Rules that make up for a model’s weaknesses expire, so keep the design principles and remove the workarounds as models get better.
- **Long-running agents need multiplayer UX.** Big jobs run for hours on async subagents, so the Slack thread shows the plan, live progress, and an approval before anything ships, and anyone on the team can steer the agent mid-run.
- **You can fork it.** The open-source repo has the full harness, and Managed Deep Agents deploys it to your team’s Slack.

‍
