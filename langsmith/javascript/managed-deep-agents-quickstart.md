# Managed Deep Agents quickstart
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/javascript/managed-deep-agents-quickstart)
Create and deploy your first Managed Deep Agent with the mda CLI.

Create an agent project, test it locally in [LangSmith Studio](../studio.md), and deploy it to managed LangSmith infrastructure with the [`mda` CLI](managed-deep-agents-cli.md). The project folder contains your agent's model, instructions, and tools. Managed Deep Agents supplies the [Deep Agents harness](https://docs.langchain.com/oss/javascript/deepagents/overview) and hosted runtime.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Prerequisites

Before you start, make sure you have:

* An organization with Managed Deep Agents public beta access.

* A [LangSmith API key](../create-account-api-key.md).

* Node.js and npm.

* An API key for your model provider of choice.

## Create and deploy an agent

### Install the package
Install `managed-deepagents`. The package includes the `mda` CLI.

```bash
npm install managed-deepagents
```

### Create a project
Create a project and open its directory:

```bash
mda init research-assistant
cd research-assistant
```

The files you edit in this quickstart are:

* **`agent.ts`**: Defines and exports the agent. See [Agent definition](managed-deep-agents-agent-definition.md).

* **[`instructions.md`](managed-deep-agents-instructions.md)**: Contains the prompt that describes how the agent should behave.

* **`.env`**: Stores API keys for local development and deployment. Do not commit this file.

For all generated files, see [Project structure](managed-deep-agents-project-structure.md).

### Add API keys
Add your LangSmith API key and model provider API key to `.env`:

```text
LANGSMITH_API_KEY=<LANGSMITH_API_KEY>
OPENAI_API_KEY=<OPENAI_API_KEY>
```

This example uses an [OpenAI chat model](https://docs.langchain.com/oss/javascript/integrations/chat/openai). If you choose another model provider, add the API key required by that provider instead. `mda deploy` uses the LangSmith API key to deploy the agent and adds the provider key to the deployment.

### Configure the agent
Open `agent.ts` and set the agent name and model:

```ts
import { defineDeepAgent } from "managed-deepagents";

export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "openai:gpt-5.5",
});
```

The model handles the agent's language understanding and reasoning. The agent name is also the default deployment name. For model concepts and provider options, see [Models](https://docs.langchain.com/oss/javascript/langchain/models).

### Edit the instructions
Open `instructions.md` and describe how the agent should behave:

```markdown
# Research assistant

You are a careful research assistant. Use internet search to find sources,
keep notes, and return concise answers with citations.
```

When you deploy, Managed Deep Agents syncs these instructions to [LangSmith Context Hub](../use-the-context-hub.md), where you can update them without redeploying the agent.

### Add an internet search tool
A tool is a function the agent can call to retrieve data or take an action. Choose your model provider's server-side search or create a [custom LangChain tool](https://docs.langchain.com/oss/javascript/langchain/tools) with Tavily.

#### Provider search (recommended)
OpenAI provides a built-in web search tool that runs server-side, so it does not require another package or API key. Add it directly to the agent:

```ts
import { defineDeepAgent } from "managed-deepagents";

export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "openai:gpt-5.5",
  tools: [{ type: "web_search_preview" }],
});
```

#### Tavily (any provider)
Add a [Tavily API key](https://app.tavily.com) to `.env`:

```text
TAVILY_API_KEY=<TAVILY_API_KEY>
```

Install the Tavily client:

```bash
npm install @langchain/tavily
```

Create a custom `internet_search` tool:

```ts
import { TavilySearch } from "@langchain/tavily";
import { tool } from "langchain";
import { z } from "zod";

export const internetSearch = tool(
  async ({ query, maxResults = 5, topic = "general" }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      topic,
    });
    return tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Search the internet for relevant sources.",
    schema: z.object({
      query: z.string().describe("The search query."),
      maxResults: z.number().optional().default(5),
      topic: z.enum(["general", "news", "finance"]).optional().default("general"),
    }),
  },
);
```

Import the tool and add it to the agent:

```ts
import { defineDeepAgent } from "managed-deepagents";

import { internetSearch } from "./tools/search";

export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "openai:gpt-5.5",
  tools: [internetSearch],
});
```

For more information, see [Custom tools](managed-deep-agents-tools.md).

### Run locally
Install the project dependencies and start the agent:

```bash
npm install
mda dev .
```

`mda dev` loads the API keys from `.env`, starts a local Agent Server, and opens the agent in LangSmith Studio. Send messages in Studio to inspect model responses and tool calls. For more information, see [Develop locally with LangSmith Studio](managed-deep-agents-local-development.md).

### Deploy the agent
Deploy the project:

```bash
mda deploy .
```

Managed Deep Agents packages the project and runs it as a hosted deployment on [LangSmith Agent Server](../agent-server.md). When deployment finishes, the CLI prints the deployment dashboard URL. Open it to view and test the deployed agent.

For deployment options and secrets handling, see [Deploy a Managed Deep Agent](managed-deep-agents-deploy.md). To inspect the agent's execution after it runs, use [LangSmith observability](../observability-quickstart.md).

## Next steps

#### [Tutorial](managed-deep-agents-tutorial.md)
Build a scheduled research agent from an empty directory.

#### [Identity](managed-deep-agents-identity.md)
Authenticate callers and provide private threads.

#### [Memory](managed-deep-agents-memory.md)
Persist preferences across threads with Context Hub `/memories`.

#### [Evals](managed-deep-agents-evals.md)
Author Harbor tasks and compile the managed agent for Harbor.

#### [Custom tools](managed-deep-agents-tools.md)
Add authored LangChain tools from your project source.

#### [MCP connectors](managed-deep-agents-mcp-connectors.md)
Add tools from remote MCP servers.

#### [Custom middleware](managed-deep-agents-middleware.md)
Add built-in or custom middleware around model and tool calls.

#### [Schedules](managed-deep-agents-schedules.md)
Run agents on managed cron schedules.

#### [Deploy an agent](managed-deep-agents-deploy.md)
Test and deploy Managed Deep Agents with `mda`.

#### [CLI reference](managed-deep-agents-cli.md)
Review `mda init`, `mda evals`, `mda dev`, and `mda deploy`.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
