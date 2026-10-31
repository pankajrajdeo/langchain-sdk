---
title: "LangSmith Observability"
description: "Traces are a series of steps that your agent takes to go from input to output. Each of these individual steps is represented by a run. You can use LangSmith to visualize these execution steps. To use..."
source: "https://docs.langchain.com/oss/javascript/langgraph/observability"
category: "docs"
tags: [docs, javascript, langgraph, observability]
---

# LangSmith Observability

Traces are a series of steps that your agent takes to go from input to output. Each of these individual steps is represented by a run. You can use [LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability) to visualize these execution steps. To use it, [enable tracing for your agent](../../langsmith/trace-with-langgraph.md). This enables you to do the following:

* [Debug a locally running agent](../../langsmith/observability-studio.md#debug-langsmith-traces).
* [Evaluate the agent performance](../langchain/test/evals.md).
* [Monitor the agent](../../langsmith/dashboards.md).

## Prerequisites

Before you begin, ensure you have the following:

* **A LangSmith account**: Sign up (for free) or log in at [smith.langchain.com](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=oss-langgraph-observability).
* **A LangSmith API key**: Follow the [Create an API key](../../langsmith/create-account-api-key.md) guide.

## Enable tracing

> [!NOTE]
>
> In an [agent-based workspace](../../langsmith/agent-registry.md), [create an agent](../../langsmith/create-an-agent.md) once before sending traces. Use [agent addressing](../../langsmith/log-traces-to-agent.md) to select its identifier and environment. If an integration requires `project_name`, use the selected environment's [`tracer_session_name`](../../langsmith/create-an-agent.md#use-an-environment-project) as a compatibility value.

To enable tracing for your agent, set the following environment variables:

```bash
export LANGSMITH_AGENT_ID="<your-agent-id>"
export LANGSMITH_AGENT_ENVIRONMENT="production"
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
```

Traces appear in the destination configured during setup.

For more information, see [Trace with LangGraph](../../langsmith/trace-with-langgraph.md).

## Trace selectively

You may opt to trace specific invocations or parts of your agent using LangSmith's `tracing_context` context manager:

```ts
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

// This WILL be traced
const tracer = new LangChainTracer();
await agent.invoke(
  {
    messages: [{role: "user", content: "Send a test email to alice@example.com"}]
  },
  { callbacks: [tracer] }
);

// This will NOT be traced (if LANGSMITH_TRACING is not set)
await agent.invoke(
  {
    messages: [{role: "user", content: "Send another email"}]
  }
);
```

## Select an agent and environment

Use `LANGSMITH_AGENT_ID` and `LANGSMITH_AGENT_ENVIRONMENT` to select the registered agent and environment. For per-request routing, pass an agent address in code. See [Log traces to an agent](../../langsmith/log-traces-to-agent.md).

> [accordion] Project-based workspaces and self-hosted LangSmith
>
> Set `LANGSMITH_PROJECT` to the tracing project name instead of setting the agent variables. For integrations that require `project_name` in an agent-based workspace, use the environment's [`tracer_session_name`](../../langsmith/create-an-agent.md#use-an-environment-project) as a compatibility value.

## Add metadata to traces

You can annotate your traces with custom metadata and tags:

```ts
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";

const tracer = new LangChainTracer();
await agent.invoke(
  {
    messages: [{role: "user", content: "Send a test email to alice@example.com"}]
  },
  config: {
    tags: ["production", "email-assistant", "v1.0"],
    metadata: {
      userId: "user123",
      sessionId: "session456",
      environment: "production"
    }
  },
);

```

This custom metadata and tags will be attached to the trace in LangSmith.

> [!TIP]
>
> To learn more about how to use traces to debug, evaluate, and monitor your agents, see the [LangSmith documentation](../../langsmith/observability.md).

## Use anonymizers to prevent logging of sensitive data in traces

You may want to mask sensitive data to prevent it from being logged to LangSmith. You can create [anonymizers](../../langsmith/mask-inputs-outputs.md#rule-based-masking-of-inputs-and-outputs) and apply them to
your graph using configuration. This example will redact anything matching the Social Security Number format XXX-XX-XXXX from traces sent to LangSmith.

**TypeScript**

```typescript
import { StateGraph } from "@langchain/langgraph";
import { LangChainTracer } from "@langchain/core/tracers/tracer_langchain";
import { StateAnnotation } from "./state.js";
import { createAnonymizer } from "langsmith/anonymizer"
import { Client } from "langsmith"

const anonymizer = createAnonymizer([
  // Matches SSNs
  { pattern: /\b\d{3}-?\d{2}-?\d{4}\b/, replace: "<ssn>" }
])

const langsmithClient = new Client({ anonymizer })
const tracer = new LangChainTracer({
  client: langsmithClient,
});

export const graph = new StateGraph(StateAnnotation)
  .compile()
  .withConfig({ callbacks: [tracer] });
```

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/langgraph/observability.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
