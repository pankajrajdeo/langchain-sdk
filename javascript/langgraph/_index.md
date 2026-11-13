---
title: "javascript/langgraph"
description: "Index of 34 pages and 2 subdirectories under javascript/langgraph."
category: "index"
tags: [index, javascript, langgraph]
---

# javascript/langgraph

34 pages here, 43 pages including subdirectories.

## Directories

- [errors/](errors/_index.md) - 6 pages
- [frontend/](frontend/_index.md) - 3 pages

## Files

- [Memory](add-memory.md) - AI applications need memory to share context across multiple interactions. In LangGraph, you can add two types of memory:
- [Build a custom RAG agent with LangGraph](agentic-rag.md) - Build a custom retrieval agent with LangGraph that decides when to search a vector store or respond directly.
- [Application structure](application-structure.md) - A LangGraph application consists of one or more graphs, a configuration file (langgraph.json), a file that specifies dependencies, and an optional .env file that specifies environment variables.
- [Backward compatibility](backward-compatibility.md) - Update LangGraph graph code in production without breaking in-flight runs.
- [Case studies](case-studies.md) - This list of companies using LangGraph and their success stories is compiled from public sources. If your company uses LangGraph, we'd love for you to share your story and add it to the list. You’re...
- [Checkpointers](checkpointers.md) - LangGraph checkpointers save graph state as checkpoints at each step, enabling persistence, human-in-the-loop, and fault-tolerant execution.
- [Deployment](deploy.md) - Deploy LangGraph agents to production with LangSmith Cloud or JavaScript frameworks and hosting platforms.
- [Event streaming](event-streaming.md) - Stream LangGraph runs with typed projections for messages, state, subgraphs, output, and extensions.
- [Fault tolerance](fault-tolerance.md) - Configure per-node timeouts, retries, error handlers, and recovery strategies in LangGraph.
- [Functional API overview](functional-api.md) - Wrap other frameworks with entrypoints and tasks for LangSmith Agent Server. Covers checkpointing, resume rules, and common pitfalls.
- [Build sequences, branches, and loops](graph-api-control-flow.md) - Compose sequences, parallel branches, conditional edges, and loops with the LangGraph Graph API.
- [Configure nodes](graph-api-nodes.md) - Add runtime configuration, retry policies, timeouts, error handling, defaults, and caching to LangGraph nodes.
- [Use Send and Command](graph-api-send-command.md) - Build map-reduce workflows with Send and combine state updates with routing using Command in LangGraph.
- [Define and update state](graph-api-state.md) - Define graph state schemas, reducers, messages, and private state in the LangGraph Graph API.
- [Visualize your graph](graph-api-visualize.md) - Render LangGraph graphs as Mermaid diagrams or PNG images for debugging and documentation.
- [Graph API overview](graph-api.md) - Learn how LangGraph models agent workflows as graphs of shared state, nodes, and edges.
- [Interrupts](interrupts.md) - Interrupts allow you to pause graph execution at specific points and wait for external input before continuing. This enables human-in-the-loop patterns where you need external input to proceed. When...
- [Run a local server](local-server.md) - This guide shows you how to run a LangGraph agent locally.
- [LangSmith Observability](observability.md) - Traces are a series of steps that your agent takes to go from input to output. Each of these individual steps is represented by a run. You can use LangSmith to visualize these execution steps. To use...
- [LangGraph overview](overview.md) - Low-level orchestration framework and runtime for long-running, stateful agents
- [Persistence](persistence.md) - LangGraph's persistence layer gives agents short-term memory through checkpointers and long-term memory through stores.
- [LangGraph runtime](pregel.md) - Pregel implements LangGraph's runtime, managing the execution of LangGraph applications.
- [Quickstart](quickstart.md) - This quickstart demonstrates how to build a calculator agent with the LangGraph Graph API.
- [Build a custom SQL agent](sql-agent.md) - In this tutorial we will build a custom agent that can answer questions about a SQL database using LangGraph.
- [Stores](stores.md) - LangGraph stores provide cross-thread long-term memory, complementing per-thread checkpointer persistence.
- [Streaming](streaming.md) - For new applications, we recommend event streaming—the typed-projection API introduced in LangGraph v1.2. Event streaming gives you separate iterators per projection (messages, values, subgraphs...
- [LangSmith Studio](studio.md) - When building agents with LangChain locally, it's helpful to visualize what's happening inside your agent, interact with it in real-time, and debug issues as they occur. LangSmith Studio is a free...
- [Test](test.md) - After you've prototyped your LangGraph agent, a natural next step is to add tests. This guide covers some useful patterns you can use when writing unit tests.
- [Thinking in the Graph API](thinking-in-graph-api.md) - Learn how to design agents with the LangGraph Graph API using nodes, edges, and shared state.
- [Agent Chat UI](ui.md) - Agent Chat UI is a Next.js application that provides a conversational interface for interacting with any LangChain agent. It supports real-time chat, tool visualization, and advanced features like...
- [Build checklist for the Graph API](use-graph-api.md) - Decide state, control flow, Send, Command, and node options as you build with the Graph API.
- [Subgraphs](use-subgraphs.md) - This guide explains the mechanics of using subgraphs. A subgraph is a graph that is used as a node in another graph.
- [Use time-travel](use-time-travel.md) - Replay past executions and fork to explore alternative paths in LangGraph
- [Workflows and agents](workflows-agents.md) - This guide reviews common workflow and agent patterns.
