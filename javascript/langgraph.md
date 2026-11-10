---
title: "LangGraph overview"
description: "Low-level orchestration framework and runtime for long-running, stateful agents"
source: "https://docs.langchain.com/oss/javascript/langgraph"
category: "docs"
tags: [docs, javascript, langgraph]
---

# LangGraph overview

> Low-level orchestration framework and runtime for long-running, stateful agents

LangGraph is a low-level orchestration framework and runtime for long-running, stateful agents. You define workflows as graphs of shared state, nodes, and edges, and can mix deterministic steps with LLM-driven steps in the same graph.

LangGraph focuses on orchestration capabilities such as [durable execution](langgraph/persistence.md), [streaming](langgraph/streaming.md), and [human-in-the-loop](langgraph/interrupts.md). It does not prescribe prompts or agent architecture.

Before you start, learn the building blocks agents use, especially [models](langchain/models.md) and [tools](langchain/tools.md). Docs examples often use [LangChain](langchain/overview.md) for those integrations, but LangGraph does not require LangChain.

If you want a higher-level agent loop first, use [Deep Agents](deepagents/overview.md) or LangChain [agents](langchain/agents.md). Use LangGraph when you need explicit control over state and control flow.

**How LangChain products fit together**

* [Deep Agents](deepagents/overview.md) is an [agent harness](concepts/products.md#agent-harnesses-like-the-deep-agents-sdk): planning, subagents, filesystem tools, and context management on top of LangGraph.
* [LangChain](langchain/overview.md) is the agent framework: abstractions and integrations for models, tools, and agent loops.
* [LangGraph](langgraph/overview.md) is the orchestration runtime: durable execution, streaming, human-in-the-loop, and persistence.
* [LangSmith](../langsmith/observability.md) is the platform for tracing, evaluation, prompts, and deployment across frameworks.
* [LangSmith Engine](../langsmith/engine.md) detects issues in LangGraph agent traces and proposes fixes. You can open a pull request with the proposed fix from the Engine tab.
* [LangSmith Fleet](../langsmith/fleet/index.md) is the no-code agent builder for templates, integrations, and routine automation.

For a comparison of the open source stack, see [Frameworks, runtimes, and harnesses](concepts/products.md).

## &#x20;Install

**npm**

```bash
npm install @langchain/langgraph @langchain/core
```

**pnpm**

```bash
pnpm add @langchain/langgraph @langchain/core
```

**yarn**

```bash
yarn add @langchain/langgraph @langchain/core
```

**bun**

```bash
bun add @langchain/langgraph @langchain/core
```

Create a minimal graph:

```typescript
import { StateSchema, MessagesValue, type GraphNode, StateGraph, START, END } from "@langchain/langgraph";

const State = new StateSchema({
  messages: MessagesValue,
});

const mockLlm: GraphNode<typeof State> = (state) => {
  return { messages: [{ role: "ai", content: "hello world" }] };
};

const graph = new StateGraph(State)
  .addNode("mock_llm", mockLlm)
  .addEdge(START, "mock_llm")
  .addEdge("mock_llm", END)
  .compile();

await graph.invoke({ messages: [{ role: "user", content: "hi!" }] });
```

For a full calculator agent, see the [LangGraph quickstart](langgraph/quickstart.md).

## Capabilities

LangGraph provides the runtime primitives for stateful, long-running workflows. It does not abstract prompts or force a fixed agent architecture.

* **Deterministic and agentic steps**: Combine hand-coded nodes with model-driven nodes in one graph.
* [**Persistence**](langgraph/persistence.md): Checkpoint state and resume after failures or pauses.
* [**Human-in-the-loop**](langgraph/interrupts.md): Pause execution, inspect or edit state, then continue.
* [**Memory**](concepts/memory.md): Short-term thread state and longer-term memory across sessions.
* [**Streaming**](langgraph/streaming.md): Stream tokens, state updates, and other events as the graph runs.

## Integrations, deployment, and observability

LangGraph works on its own. However, you can also pair it with other LangChain products:

> [card] [LangChain](langchain/overview.md)
>
> Integrations and agent abstractions built on LangGraph.

> [card] [LangSmith Deployment](../langsmith/deployment.md)
>
> Deploy and scale stateful agents, with visual prototyping in Studio.

> [card] [LangSmith Observability](../langsmith/observability.md)
>
> Trace requests, evaluate outputs, and monitor deployments.

## See also

* [LangGraph quickstart](langgraph/quickstart.md)
* [Graph API overview](langgraph/graph-api.md)
* [Frameworks, runtimes, and harnesses](concepts/products.md)
* [Incorporate existing code and other frameworks](../langsmith/deploy-other-frameworks.md) (wrap a non-LangGraph agent for LangSmith Deployment)

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
