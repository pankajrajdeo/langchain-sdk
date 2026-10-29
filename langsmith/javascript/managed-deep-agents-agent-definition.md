---
title: "Define a Managed Deep Agent"
description: "Configure the model and core capabilities of a managed deep agent."
source: "https://docs.langchain.com/langsmith/javascript/managed-deep-agents-agent-definition"
category: "docs"
tags: [docs, langsmith, javascript, managed-deep-agents-agent-definition]
---

# Define a Managed Deep Agent

> Configure the model and core capabilities of a managed deep agent.

The agent definition selects the model and core capabilities of a managed deep agent.

> [!NOTE]
>
> Managed Deep Agents is in **public [beta](../release-stages.md)** on [LangSmith Cloud](../cloud.md).

The agent entry lives at the project root:

```text
my-agent/
  agent.ts
```

You can also use `agent.tsx`.

For the full project layout, see [Project structure](managed-deep-agents-project-structure.md).

To define the agent, use `defineDeepAgent`:

**OpenAI**

```ts
import { defineDeepAgent } from "managed-deepagents";

export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "openai:gpt-5.5",
});
```

**Anthropic**

```ts
import { defineDeepAgent } from "managed-deepagents";

export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "anthropic:claude-sonnet-4-6",
});
```

**Google Gemini**

```ts
import { defineDeepAgent } from "managed-deepagents";

export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "google:gemini-3.6-flash",
});
```

**Microsoft Foundry**

```ts
// To use ChatOpenAI, run: npm install @langchain/openai
import { defineDeepAgent } from "managed-deepagents";
import { ChatOpenAI } from "@langchain/openai";

const model = new ChatOpenAI({
  model: process.env.AZURE_OPENAI_DEPLOYMENT_NAME,
  apiKey: process.env.AZURE_OPENAI_API_KEY,
  configuration: {
    baseURL: process.env.AZURE_AI_OPENAI_ENDPOINT,
  },
});

export const agent = defineDeepAgent({
  name: "research-assistant",
  model,
});
```

Configure the system prompt, skills, memory, sandbox, identity, channels, and schedules through their project files rather than the agent definition. See [Project structure](managed-deep-agents-project-structure.md). To select the system prompt, skills, MCP servers, or sandbox for each run, see [Select configuration per run](#select-configuration-per-run).

`defineDeepAgent` does not compile an agent. It returns a definition, and the managed runtime compiles it with [createDeepAgent](https://reference.langchain.com/javascript/deepagents/agent/createDeepAgent) at deploy time. The options below are the [createDeepAgent](https://reference.langchain.com/javascript/deepagents/agent/createDeepAgent) surface without the ones the runtime owns. See [Relationship to Deep Agents](managed-deep-agents-overview.md#relationship-to-deep-agents).

## Parameters

| Parameter | What it does |
| - | - |
| `name` | Required. Set the agent and default deployment name. Pass a static string that starts with a letter and contains only letters, numbers, underscores, or hyphens, such as `"research-assistant"`.  Managed Deep Agents uses the name as the agent's graph ID and the default LangSmith deployment name, and clients pass it as `assistantId` when they call the deployment. You can override the deployment name with `mda deploy --name` without changing the agent definition. |
| `model` | Set the chat model the agent uses. The simplest option is a `provider:model` string. Add the provider's API key to `.env` so the model works locally and in the deployment.  Pass a LangChain chat model instance instead when you need to configure model parameters in code. For model options and supported providers, see [Models](../../javascript/deepagents/models.md).  To connect to LLM Gateway, see [Use LLM Gateway](#use-llm-gateway). |
| `tools` | Add tools the agent can call. Pass tools in the `tools` array so the agent can call application logic or external services.  Define tools in local modules, import them into the agent entry, and add them to the definition. See [Custom tools](managed-deep-agents-tools.md). To add tools from remote MCP servers without importing them into the agent entry, use [MCP connectors](managed-deep-agents-mcp-connectors.md). |
| `middleware` | Add behavior around model calls, tool calls, and the agent lifecycle. Pass middleware in the `middleware` array. Middleware runs in array order. See [Custom middleware](managed-deep-agents-middleware.md). |
| `subagents` | Define specialized agents for delegated tasks. Pass subagent definitions when the agent should delegate specialized or context-heavy work. Each subagent can have its own prompt, model, and tools. See [Subagents](managed-deep-agents-subagents.md), including how to run a subagent in the background. |
| `permissions` | Control path-level access for filesystem tools. Pass filesystem permission rules to control which paths the agent's built-in filesystem tools can read or write. Cleared when the project declares a [sandbox](managed-deep-agents-sandboxes.md), because a permission rule disables the sandbox `execute` tool. See [Permissions](../../javascript/deepagents/permissions.md). |
| `interruptOn` | Pause before selected tool calls for human approval. Set `interruptOn` to pause before selected tool calls, so a person can approve, edit, or reject the call before it runs. See [Human-in-the-loop](managed-deep-agents-tools.md#human-in-the-loop). |
| `responseFormat` | Set when the agent must return data that matches a schema instead of an unconstrained text response. See [Structured output](../../javascript/langchain/structured-output.md). |

## Select configuration per run

To select the agent's configuration for each run, export a function as `agent` instead of a definition. One deployment can then adapt to different users, tasks, or repositories. The function is a graph factory, the same pattern LangGraph uses to [rebuild a graph at runtime](../graph-rebuild.md): it receives the runtime and returns a definition.

This example selects instructions and skills for the repository a run works on. It assumes the project has `skills/python-service/` and `skills/typescript-web/`, each with a [`SKILL.md`](managed-deep-agents-skills.md).

**agent.ts**

```ts
import { defineDeepAgent, type ManagedServerRuntime } from "managed-deepagents";
import { z } from "zod";

const contextSchema = z.object({ repository: z.string().optional() });

export function agent(
  runtime: ManagedServerRuntime<z.infer<typeof contextSchema>>
) {
  const context = runtime.executionRuntime?.context;
  const pythonService = context?.repository === "payments-service";

  return defineDeepAgent({
    name: "open-swe",
    model: "openai:gpt-5.5",
    instructions: pythonService
      ? "Follow the payments service's API and reliability conventions."
      : "Follow the storefront's frontend and accessibility conventions.",
    skills: [pythonService ? "./skills/python-service" : "./skills/typescript-web"],
    contextSchema,
  });
}
```

The factory can be sync or async. It receives a `ManagedServerRuntime`, which extends the native LangGraph `ServerRuntime`. Read run context from `executionRuntime.context`. It is `undefined` on channel runs, and `executionRuntime` is `null` when Agent Server loads the agent for inspection.

Callers choose the configuration through the run's `context`:

```ts
await client.runs.create(threadId, "open-swe", {
  input: { messages: [{ role: "user", content: "Run the service test suite." }] },
  context: { repository: "payments-service" },
});
```

Run context is application data, not verified identity. Check authorization in [tools](managed-deep-agents-tools.md) against the verified caller on the runtime.

### Select managed resources

A factory can also select the resources that a static agent reads from project files. Omitting a field keeps the project's configuration. Providing a value replaces it for that run:

| Field | Omitted | Selected | Cleared |
| - | - | - | - |
| `instructions` | Uses `instructions.md`. | Uses the supplied prompt. | `""` removes authored instructions. |
| `skills` | Exposes all project skills. | Exposes only the selected skills. | `[]` exposes no skills. |
| `mcp` | Uses the `mcp` declaration. | Uses only the selected MCP definitions. | `[]` exposes no MCP tools. |
| `sandbox` | Uses the `sandbox` declaration. | Uses the supplied sandbox. | `null` disables the sandbox. |
| `browser` | Uses root `browser.ts`. | Uses the supplied browser definition. | `null` disables browser tools. |

> [!NOTE]
>
> Browser declarations and per-run selection were added in SDK 0.10. Keep a root `browser.ts` even when the factory selects a browser. See [Choose a browser per run](managed-deep-agents-browser-use.md#choose-a-browser-per-run).

Static definitions cannot set these fields. A skill path must end in `skills/<name>` and point to a skill in the project. A factory can also return generated skill definitions, whose names must not duplicate project skill names.

This example enables the docs MCP server on request and gives one repository a longer sandbox timeout. It imports the declarations from [`tools/mcp`](managed-deep-agents-mcp-connectors.md) and [`sandbox/`](managed-deep-agents-sandboxes.md):

**agent.ts**

```ts
import {
  defineDeepAgent,
  defineSandbox,
  type ManagedServerRuntime,
} from "managed-deepagents";
import { z } from "zod";

import { sandbox } from "./sandbox/index";
import { mcp } from "./tools/mcp";

const contextSchema = z.object({
  repository: z.string().optional(),
  needsDocs: z.boolean().optional(),
});

export function agent(
  runtime: ManagedServerRuntime<z.infer<typeof contextSchema>>
) {
  const context = runtime.executionRuntime?.context;
  const pythonService = context?.repository === "payments-service";

  return defineDeepAgent({
    name: "open-swe",
    model: "openai:gpt-5.5",
    mcp: context?.needsDocs ? [mcp] : [],
    sandbox: pythonService ? defineSandbox({ defaultTimeout: 600 }) : sandbox,
    contextSchema,
  });
}
```

Memory is not selected per run. Declare it in the project's memory file, and control access for each run with an `allow` policy. See [Control access to a layer](managed-deep-agents-memory.md#control-access-to-a-layer).

### Keep the factory repeatable

Managed Deep Agents calls the factory at the start of each run, and again when a run resumes or retries. Agent Server also calls it to read schemas and state. Follow these rules:

* **No side effects**: Return the same definition for the same context. Do not create records, call external APIs, or change shared state in the factory.
* **Stable interrupts**: Keep middleware that can interrupt a run in every configuration. When a run resumes, the middleware that raised the interrupt must still be present.
* **Inline name**: Set `name` as an inline string. `mda build` reads it without calling the factory and uses it as the graph ID and default deployment name.
* **Model dependencies**: Install the integration package for every model the factory can return. The build does not detect them.

To change behavior between model calls within a run, use [custom middleware](managed-deep-agents-middleware.md).

## Use LLM Gateway

You can use [LLM Gateway](../llm-gateway.md) to apply rate limits, fallbacks, and other policies to model calls.

Prefix the gateway model ID with `langsmith:`:

```ts
import { defineDeepAgent } from "managed-deepagents";

export const agent = defineDeepAgent({
  name: "my-agent",
  model: "langsmith:moonshotai/kimi-k3",
});
```

> [!NOTE]
>
> Gateway model IDs use a slash between provider and model (`langsmith:provider/model-name`). Model strings that call a provider directly use a colon (`provider:model-name`).

The gateway routes each request by model ID. `moonshotai/kimi-k3` is a LangChain-hosted model, so it requires no provider secret and draws on [Gateway Credits](../llm-gateway-credits.md). A model ID that starts with a provider your workspace has configured, such as `anthropic/claude-opus-5`, uses that [provider secret](../llm-gateway-admin-setup.md#1-add-provider-secrets) and bills to your own provider account.

For more information, see [LLM Gateway](../llm-gateway.md).

To scaffold a project that uses Gateway from the start, pass `--gateway` when initializing:

```bash
mda init my-agent --gateway
```

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-agent-definition.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
