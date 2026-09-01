# Managed Deep Agents quickstart

> Create and deploy your first Managed Deep Agent with the mda CLI.

Create and deploy your first Managed Deep Agent: scaffold a project, configure the model and instructions, add search, test in [LangSmith Studio](../studio.md), and deploy with the [`mda` CLI](managed-deep-agents-cli.md). Managed Deep Agents supplies the [Deep Agents harness](https://docs.langchain.com/oss/javascript/deepagents/overview) and hosted runtime.

After this quickstart, the [tutorial](managed-deep-agents-tutorial.md) adds durable memory and a daily schedule on the same project.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Prerequisites

To follow along, you need:

* Node.js and npm.

* An API key for your model provider of choice.

## Add the `managed-deep-agents` skill

The [`managed-deep-agents` skill](https://github.com/langchain-ai/langchain-skills/blob/main/config/skills/managed-deep-agents/SKILL.md) walks a coding agent through building, testing, and deploying a Managed Deep Agent with the `mda` CLI. To add it to the current project, run:

```bash
npx skills add langchain-ai/langchain-skills --skill managed-deep-agents --yes
```

## Create and deploy an agent

### Set up the project
Create a project and open its directory:

```bash
npx managed-deepagents init research-assistant
cd research-assistant
```

```bash
pnpm dlx managed-deepagents init research-assistant
cd research-assistant
```

```bash
bunx managed-deepagents init research-assistant
cd research-assistant
```

You now have all the scaffolding for your agent.

### Add your keys
Add your model provider API key to `.env`:

```text
OPENAI_API_KEY=<OPENAI_API_KEY>
# ANTHROPIC_API_KEY=<ANTHROPIC_API_KEY>
# GOOGLE_API_KEY=<GOOGLE_API_KEY>
```

This quickstart uses OpenAI by default. If you choose Google or Anthropic in the next step, set that provider's API key instead. `mda deploy` adds the provider key to the deployment. You can also use any [other chat provider](https://docs.langchain.com/oss/javascript/integrations/chat/).

> [!WARNING]
> Do not commit the `.env` file into version control. It contains secrets.

### Set up LangSmith
Managed Deep Agents runs on LangSmith. Your LangSmith API key authenticates local development with `mda dev`, deploys the agent with `mda deploy`, and opens the agent in [LangSmith Studio](../studio.md) so you can chat with it and inspect traces.

[Sign up for LangSmith](https://smith.langchain.com?utm_source=docs\&utm_medium=cta\&utm_campaign=langsmith-signup\&utm_content=langsmith-managed-deep-agents-quickstart) if you do not already have an account.

To create a LangSmith API key, open [Settings](https://smith.langchain.com/settings), go to **API Keys**, and click **Create API Key**. For more details, see [Create an account and API key](../create-account-api-key.md).

Add your LangSmith API key to `.env`:

```text
LANGSMITH_API_KEY=<LANGSMITH_API_KEY>
```

### Edit the instructions
Open `instructions.md` and describe how the agent should behave:

```markdown
# Research assistant

You are a careful research assistant. Use internet search to find sources,
keep notes, and return concise answers with citations.
```

When you deploy, Managed Deep Agents syncs these instructions to [LangSmith Context Hub](../use-the-context-hub.md), where you can update them without redeploying the agent.

### Configure your model and search
Now set the model and a built-in web search tool. Google, OpenAI, and Anthropic offer server-side search with no extra package or API key. Pass the provider tool dict that matches your model:

Open `agent.ts`:

```ts
import { defineDeepAgent } from "managed-deepagents";

// OpenAI's built-in web search — no extra install or API key needed
export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "openai:gpt-5.5",
  tools: [{ type: "web_search_preview" }],
});
```

```ts
import { defineDeepAgent } from "managed-deepagents";

// Google's built-in search — no extra install or API key needed
export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "google-genai:gemini-3.6-flash",
  tools: [{ google_search: {} }],
});
```

```ts
import { defineDeepAgent } from "managed-deepagents";

// Anthropic's built-in web search — no extra install or API key needed
export const agent = defineDeepAgent({
  name: "research-assistant",
  model: "anthropic:claude-sonnet-4-6",
  tools: [{ type: "web_search_20250305", name: "web_search" }],
});
```

The agent name is also the default deployment name. For model concepts and provider options, see [Models](https://docs.langchain.com/oss/javascript/langchain/models).

<details>
<summary>Using another provider?</summary>

You can use a Tavily search tool instead.
Add a [Tavily API key](https://app.tavily.com) to `.env`:

```text
TAVILY_API_KEY=<TAVILY_API_KEY>
```

Install the Tavily client:

```bash
npm install @langchain/tavily
```

```bash
pnpm add @langchain/tavily
```

```bash
bun add @langchain/tavily
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

For more authored tools, see [Custom tools](managed-deep-agents-tools.md).

</details>

### Run locally
Install the project dependencies and start the agent:

```bash
npm install
npx mda dev
```

```bash
pnpm install
pnpm exec mda dev
```

```bash
bun install
bunx mda dev
```

`mda dev` loads the API keys from `.env`, starts a local Agent Server, and opens the agent in LangSmith Studio.

In Studio, send:

```txt
What were the main announcements from the latest LangChain release?
```

You should see the agent call the web search tool, then return a concise answer that cites sources. If search never appears in the trace, confirm the provider tool dict matches the model you set in `agent.py` or `agent.ts`.

For more information, see [Develop locally with LangSmith Studio](managed-deep-agents-local-development.md).

### Deploy the agent
Deploy the project by running:

```bash
npx mda deploy
```

```bash
pnpm exec mda deploy
```

```bash
bunx mda deploy
```

Managed Deep Agents packages the project and runs it as a hosted deployment on [LangSmith Agent Server](../agent-server.md). When deployment finishes, the CLI prints the deployment dashboard URL.

Open that URL. You should see the deployment in a ready state. Send the same research question from the previous step and confirm the hosted agent returns an answer with a search tool call. For deployment options and secrets handling, see [Deploy a Managed Deep Agent](managed-deep-agents-deploy.md). To inspect the agent's execution after it runs, use [LangSmith observability](../observability-quickstart.md).

## Next steps

#### [Tutorial](managed-deep-agents-tutorial.md)
Add a custom Tavily search tool, durable memory, and a daily schedule.

#### [Custom tools](managed-deep-agents-tools.md)
Add authored LangChain tools from your project.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-quickstart.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
