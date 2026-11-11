---
title: "How Workday Built an Enterprise-Scale AI Agent Platform with LangGraph and LangSmith"
description: "See how Workday used LangGraph and LangSmith to build an internal AI agent platform that cut prototype time from months to less than a day and compliance needs."
source: "https://www.langchain.com/blog/how-workday-built-an-enterprise-scale-ai-agent-platform-with-langgraph-and-langsmith"
category: "blog"
published: "2026-11-10T16:00:00.000Z"
author: "LangChain Accounts"
tags: [blog, how-workday-built-an-enterprise-scale-ai-agent-platform-with-langgraph-and-langsmith]
---

# How Workday Built an Enterprise-Scale AI Agent Platform with LangGraph and LangSmith

[Workday](https://www.workday.com/) is the trusted agentic platform for HR, finance, and IT, serving more than half the Fortune 500. The team set out to create the internal developer platform to build, deploy, and run AI agents in production, on Workday's infrastructure. The team leveraged LangGraph for agent orchestration and LangSmith for tracing, observability, and evals.

## Shipping an agent platform fast, with a team of 4

In 2025, Workday’s leadership team saw the market opportunity for building agentic solutions and set an ambitious goal for agents in production by the end of 2026. Product teams needed a platform that could support both rapid prototyping and production deployments—a uniquely challenging mandate given Workday operates under some of the strictest security and data governance requirements in enterprise software. Getting any internal service into production means satisfying demanding audit, compliance, and data retention policies.

The surface area was enormous for a team of four, encompassing a durable, scalable agent server; data access controls tied to Workday's audit policies; a collaborative eval platform; and an SDK that abstracted all of it.

## Built for builders: abstracting infrastructure for Workday's agent teams

Workday’s Agent Platform team serves two user bases. 1.) the internal Workday engineering teams building agents, and 2.) the end customers of those agents. It lets teams focus on functional requirements, while handling authentication, security, compliance, and infrastructure.

The first major product shipped was Workday's Agent System of Record, a governance layer that controls which APIs the agents are allowed to access. The Agent Platform team built the backend server and eval infrastructure that the system of record runs on top of.

The team also built what Alex Gatto, Senior Machine Learning Engineer, describes as "Workday LangChain": a Python SDK that wraps LangChain primitives and routes them through Workday's internal services, including an LLM gateway, a RAG retrieval service, and other internal tooling. "Anytime there was some AI concept that LangChain had put out, we tried to build a Python SDK for that same concept, but at Workday," explained Alex.

## LangGraph and LangSmith for design flexibility without backend overhead

Workday chose LangGraph for agent orchestration to give internal developers maximum flexibility at the design layer, while providing standardized infrastructure underneath.

Compared to platforms that modeled agents as sequences of conversations or personas, LangGraph’s graph-based model gave engineers the power to build everything from simple ReAct loops to complex deterministic workflows, without the platform prejudging what an agent should look like.

“One of my favorite things about LangChain’s Agent Server and LangSmith is just how much you get for free. Just because of how much they've thought about agent development,” said Alex. For example, when senior leadership asked the team about Workday's strategy for A2A and MCP protocols, the team could immediately answer that it was already in production.

Because LangChain's agent server implementations are built with A2A and MCP support, every agent server the Agent Platform team ran was already compliant with both protocols. Any developer update to their graph was immediately reflected in the server. "The backend isn't the problem," Alex reported. "LangChain took care of it for us."

## Time-to-prototype reduced from 5 months to less than 1 day

Previously, building a prototype agent took 4 to 5 months, with no guarantee it could ever reach production. With the new platform, a team can have a prototype running in a staging environment in under a day, with authentication and security requirements baked in. The only question left for the agent-building team is: what does this agent actually do, and what does the graph look like?

The team, which started at 4 people, has now grown to roughly 30 members, with continued investment planned. “Because of the success of our partnership with LangChain and what we were able to accomplish, we’ve more than tripled the size of our team,” said Alex.

For Alex, the platform represents something bigger than an agent deployment layer. Workday engineers have built dozens of internal services over the years (LLM gateways, RAG retrievers, recommendation engines, prompt services) most of which existed in isolation, unknown outside their immediate teams. Agent Platform, with its Python SDKs and LangChain-backed primitives, became the connectivity layer that surfaced all of it; it’s the first unified interface for building agents that actually taps into the full depth of Workday's internal infrastructure.

"Our partnership with LangChain is critical to our agent development,” said Alex. “You're gaining a really deep partnership when we work with them. And there's just no way that we could have delivered value to our customers without LangSmith’s speed and maturity.”

‍

*Building production agent infrastructure? Learn more about *[*LangGraph*](https://langchain-ai.github.io/langgraph/)*, and LangSmith for *[*Deployment*](https://www.langchain.com/langsmith/deployment)* and *[*Observability*](https://www.langchain.com/langsmith/observability)*.*
