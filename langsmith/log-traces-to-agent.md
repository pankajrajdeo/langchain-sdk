---
title: "Log traces to an agent"
description: "How agent addressing sends traces to an agent and an environment, which variables carry it, and why it cannot be combined with project addressing."
source: "https://docs.langchain.com/langsmith/log-traces-to-agent"
category: "docs"
tags: [docs, langsmith, log-traces-to-agent]
---

# Log traces to an agent

> How agent addressing sends traces to an agent and an environment, which variables carry it, and why it cannot be combined with project addressing.

*Agent addressing* names the [agent](agents.md) and the [environment](agent-environments.md) a trace belongs to. Your application sends both with every run, and LangSmith records them when the trace arrives. A trace uses either agent addressing or [project addressing](log-traces-to-project.md), never both.

> [!NOTE]
> Agent addressing applies to agent-based workspaces, which are in [beta](release-stages.md). The [`address` argument](#addressing-arguments) can change without notice. Agent addressing is supported in:
>
> * The Python SDK from `langsmith>=0.14.4`
> * The TypeScript SDK from `langsmith>=0.10.8`
>
> For tracing setup that does not depend on the beta, see [Log traces to a specific project](log-traces-to-project.md).

## Addressing variables

Two environment variables carry agent addressing:

* **`LANGSMITH_AGENT_ID`**: The agent to address. The value is the agent's identifier, which the browser address bar carries and the **ID** field on the agent's Overview copies. It is sent with every run.
* **`LANGSMITH_AGENT_ENVIRONMENT`**: The environment the run belongs to. Required alongside the agent, and one of `local`, `development`, `staging`, or `production`. Use the lowercase form, which maps to the Local, Development, Staging, and Production labels in the UI. There is no default, because neither the agent nor the environment names a destination alone. If only one of the two variables is set, the SDK logs a warning and leaves the call untraced instead of picking an environment for you, so nothing reaches LangSmith.

`LANGSMITH_AGENT_ID` takes the identifier, not the display name. A [display name is a separate, editable value](agents.md#identifiers-and-display-names) that does not have to match the identifier, so read the identifier from the agent rather than deriving it from what the agent is called.

## Addressing arguments

Supply the agent and the environment together, as one address in code or as both [environment variables](#addressing-variables). An address is a single string, `lrn:agents/{id}/environments/{environment}`. Build it with `ls.address.agent("checkout", "production")` in Python or `address.agent("checkout", "production")` in TypeScript, which checks both values and lowercases the environment, or write the string directly.

In Python, [`@traceable`](https://reference.langchain.com/python/langsmith/run_helpers/traceable) and [`tracing_context`](https://reference.langchain.com/python/langsmith/run_helpers/tracing_context) each accept `address`. In TypeScript, [`traceable`](https://reference.langchain.com/javascript/langsmith/traceable) accepts `address` in its config. An address in code takes precedence over the variables. The SDK reads the variables only when nothing in code names a destination, and then it needs both.

## Examples

Address one function with the decorator:

```python
import langsmith as ls
from langsmith import traceable

@traceable(address=ls.address.agent("checkout", "production"))
def handle_order(order_id: str) -> dict:
    return {"order_id": order_id, "status": "charged"}
```

Address everything traced inside a block with the context manager:

```python
from langsmith import traceable, tracing_context

@traceable
def handle_order(order_id: str) -> dict:
    return {"order_id": order_id, "status": "charged"}

with tracing_context(address="lrn:agents/checkout/environments/production"):
    handle_order("A-1")
```

Address a function in TypeScript:

```typescript
import { address } from "langsmith";
import { traceable } from "langsmith/traceable";

const handleOrder = traceable(
  async (orderId: string) => ({ orderId, status: "charged" }),
  { name: "handle_order", address: address.agent("checkout", "production") },
);
```

## Send your first agent-addressed trace

### Confirm your workspace is enabled
If your workspace is agent-based, agent addressing is already on. LangChain turns it on, and you have no setting to change. In a workspace that LangChain [converted](migrate-to-agent-based-workspaces.md#how-a-workspace-moves), an admin can switch the UI between the new and the classic experience. That switch changes only what the UI shows. It does not turn on agent addressing.

To tell which kind of workspace you have, look at the control at the top left. In an agent-based workspace it names your workspace. In a project-based workspace it shows the LangSmith logo, and agent addressing is off. To ask about access, [contact our sales team](https://www.langchain.com/contact-sales).

If your workspace is not enabled, LangSmith ingestion rejects agent-addressed runs and records nothing.

### Install the SDK
Agent addressing needs `langsmith>=0.14.4` in Python or `langsmith@>=0.10.8` in TypeScript:

**uv**

```bash
uv add "langsmith>=0.14.4"
```

**pip**

```bash
pip install -U "langsmith>=0.14.4"
```

**npm**

```bash
npm install "langsmith@>=0.10.8"
```

### Choose an identifier
Copy the identifier from the **ID** field on an existing agent's Overview, or pick a new one. If no agent in the workspace uses the identifier you pick, LangSmith creates that agent the first time you send a trace to it. You do not have to create the agent in advance. For the rules an identifier must follow, see [Identifier rules](create-an-agent.md#identifier-rules).

### Configure the addressing
Set both addressing [variables](#addressing-variables), or pass an [address](#addressing-arguments) in code. If only one variable is set, the SDK logs a warning and sends nothing.

```bash
export LANGSMITH_TRACING=true
export LANGSMITH_API_KEY=<your-api-key>
export LANGSMITH_AGENT_ID=checkout
export LANGSMITH_AGENT_ENVIRONMENT=production
```

The first two are the usual tracing prerequisites rather than part of agent addressing. Use an [API key](create-account-api-key.md) from the workspace you confirmed in step 1.

### Run your application
Run your application so it sends at least one trace. Producing traces needs `@traceable` or `tracing_context` in Python, or `traceable` in TypeScript, as in [Examples](#examples).

### Find the trace
In LangSmith, select the agent in the top bar, go to **Tracing**, and set the environment control to the one you addressed. The trace appears there.

## Addressing modes are mutually exclusive

Agent addressing and project addressing do not combine. What happens depends on where each is set:

* **An agent and a project together**: Not allowed. If you set the agent variables and also `LANGSMITH_PROJECT`, `LANGCHAIN_PROJECT`, or `LANGCHAIN_SESSION`, the trace has two destinations, and the SDK does not pick one. It logs a warning when the client starts, and it does not trace a call unless code names the destination. If you pass both `address` and `project_name` to `@traceable` or `tracing_context()` in one call, the SDK raises `LangSmithUserError` and sends nothing. If a run with both an address and a project reaches LangSmith, LangSmith rejects it.
* **A project named in code**: Overrides the agent variables. Passing `project_name` to `@traceable` or `tracing_context()` traces the run to that project and ignores the agent variables, without an error. This is what lets an [evaluation](evaluation.md) set its own project while the agent variables stay set for the rest of the process.

## Addressing an agent that does not exist

If an identifier does not match an agent in the workspace, LangSmith creates that agent.

For the rules the value must follow, see [Identifier rules](create-an-agent.md#identifier-rules).

An agent created this way shows no Deployments section on its [Overview](navigate-agents.md#read-the-agent-overview).

## When runs stop being accepted

A workspace that accepted agent-addressed runs can stop accepting them. First check that your API key still belongs to the agent-based workspace, because LangSmith rejects agent-addressed runs sent with a key from a project-based workspace. If the key is not the problem, contact support via [support.langchain.com](https://support.langchain.com).

## See also

* [Agents](agents.md)
* [Agent environments](agent-environments.md)
* [Log traces to a specific project](log-traces-to-project.md)
* [Observability concepts](observability-concepts.md)

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/log-traces-to-agent.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
