---
title: "Learn"
description: "Tutorials, conceptual guides, and resources to help you get started."
source: "https://docs.langchain.com/oss/javascript/learn"
category: "docs"
tags: [docs, javascript, learn]
---

# Learn

> Tutorials, conceptual guides, and resources to help you get started.

In the **Learn** section of the documentation, you will find a collection of tutorials, conceptual overviews, and additional resources to help you build powerful applications with Managed Deep Agents, Deep Agents, LangChain, and LangGraph.

## Tutorials

Below are tutorials for common use cases, organized by framework.

### Managed Deep Agents

[Managed Deep Agents](../langsmith/javascript/managed-deep-agents-overview.md) is the recommended way to build and deploy deep agents. You write the agent; LangSmith runs the harness and runtime.

> **[Deep research](deepagents/deep-research.md)**
>
> Build a multi-step web research agent with Managed Deep Agents or the Deep Agents SDK.

> **[Content builder](deepagents/content-builder.md)**
>
> Build a content writing agent with brand voice, skills, and image tools using Managed Deep Agents or the Deep Agents SDK.

### Deep Agents

For maximum flexibility while using the same Deep Agents harness as [Managed Deep Agents](#managed-deep-agents), use the Deep Agents SDK and host agents yourself, or run a custom [LangSmith Deployment](../langsmith/deployment.md).

> **[Deep research](deepagents/deep-research.md)**
>
> Build a multi-step web research agent with Managed Deep Agents or the Deep Agents SDK.

> **[Content builder](deepagents/content-builder.md)**
>
> Build a content writing agent with brand voice, skills, and image tools using Managed Deep Agents or the Deep Agents SDK.

### LangChain

[LangChain](langchain/overview.md) [agent](langchain/agents.md) implementations make it easy to get started for simple use cases.

> **[Semantic Search](langchain/knowledge-base.md)**
>
> Build a semantic search engine over a PDF with LangChain components.

> **[RAG Agent](deepagents/rag.md)**
>
> Create a Retrieval Augmented Generation (RAG) agent.

> **[SQL Agent](langchain/sql-agent.md)**
>
> Build a SQL agent to interact with databases with human-in-the-loop review.

> **[Voice Agent](langchain/voice-agent.md)**
>
> Build an agent you can speak and listen to.

### LangGraph

LangChain's [agent](langchain/agents.md) implementations use [LangGraph](langgraph/overview.md) primitives.
If deeper customization is required, agents can be implemented directly in LangGraph.

> **[Custom RAG Agent](langgraph/agentic-rag.md)**
>
> Build a RAG agent using LangGraph primitives for fine-grained control.

> **[Custom SQL Agent](langgraph/sql-agent.md)**
>
> Implement a SQL agent directly in LangGraph for maximum flexibility.

### Multi-agent

These tutorials demonstrate [multi-agent patterns](langchain/multi-agent.md), blending LangChain agents with LangGraph workflows.

## Conceptual overviews

These guides explain the core concepts and APIs underlying LangChain and LangGraph.

> **[Memory](concepts/memory.md)**
>
> Understand persistence of interactions within and across threads.

> **[Context engineering](concepts/context.md)**
>
> Learn methods for providing AI applications the right information and tools to accomplish a task.

> **[Graph API](langgraph/graph-api.md)**
>
> Explore LangGraph’s declarative graph-building API.

> **[Functional API](langgraph/functional-api.md)**
>
> Build agents as a single function.

## Additional resources

> **[LangChain Academy](https://academy.langchain.com/)**
>
> Courses and exercises to level up your LangChain skills.

> **[Case Studies](langgraph/case-studies.md)**
>
> See how teams are using LangChain and LangGraph in production.

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/learn.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
