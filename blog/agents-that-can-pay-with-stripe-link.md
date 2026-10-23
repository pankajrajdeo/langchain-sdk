---
title: "Agents that can pay: building Restock with Stripe&#39;s Link and Managed Deep Agents"
description: "Build an agent that pays for real purchases. Restock runs in Slack on Managed Deep Agents and pays with Stripe&#39;s Link over the Machine Payments Protocol."
source: "https://www.langchain.com/blog/agents-that-can-pay-with-stripe-link"
category: "blog"
published: "2026-10-08T15:55:00.000Z"
author: "LangChain Accounts"
tags: [blog, agents-that-can-pay-with-stripe-link]
---

# Agents that can pay: building Restock with Stripe&#39;s Link and Managed Deep Agents

- **Restock is a sample agent that pays for real purchases.** It runs in Slack on Managed Deep Agents, finds products, builds a cart, and checks out through an API that supports the [Machine Payments Protocol](https://mpp.dev/overview) (MPP).
- **Payments stay safe and within budget.** Link, Stripe's consumer wallet, handles the payment, so the agent never sees a card number. The user approves a spend request up to a set amount, and the agent can't spend above it.
- **Build your own agent that can pay.** Start from [Restock's sample code](https://github.com/langchain-samples/restock-agent), and let us know what you build.
