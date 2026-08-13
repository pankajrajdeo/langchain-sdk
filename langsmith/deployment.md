# LangSmith Deployment
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/deployment)
Deploy and manage agents with durable execution, real-time streaming, and horizontal scaling.

**LangSmith Deployment** is a workflow orchestration runtime purpose-built for agent workloads. It provides the managed infrastructure agents need to run reliably in production at scale, supporting the full lifecycle from local development to deployment.

> [!NOTE]
> This page covers how your **agents** run in production with **LangSmith Deployment**.
>
> Where you run LangSmith for observability, evaluation, and prompt engineering is separate; refer to [Platform setup](platform-setup.md) for details.

## Deployable products

LangSmith Deployment is framework-agnostic which means you can deploy agents built with:

#### [LangGraph (and LangChain)](deployment-quickstart.md)
Use the LangGraph CLI and app templates to deploy an application to LangSmith.

#### [Google ADK](deploy-google-adk.md)
Deploy Google Agent Development Kit (ADK) agent as a LangGraph with the `deployments-wrap-sdk` package.

#### [Other frameworks](deploy-other-frameworks.md)
Deploy Claude Agent SDK, Strands, CrewAI, AutoGen, and other agent frameworks with the Functional API or `deployments-wrap-sdk`.

#### [Looking to deploy Deep Agents?](python/managed-deep-agents-overview.md)
Use Managed Deep Agents: the managed runtime for deploying code-first Deep Agents.

## LangSmith Deployment environments

Pick an environment based on where you want the [control plane](control-plane.md) and [data plane](data-plane.md) (Agent Servers and their databases) to run. All infrastructure types use the same [Agent Server](agent-server.md) runtime.

#### [Cloud](deploy-to-cloud-overview.md)
Fully managed by LangChain on AWS and GCP. Create deployments from GitHub in the LangSmith UI or with [`langgraph deploy`](cli.md#deploy). Requires a [Plus plan or above](https://www.langchain.com/pricing).

#### [Self-hosted with control plane](deploy-with-control-plane.md)
Run the LangSmith Deployment control plane and Agent Servers in your own Kubernetes cluster, alongside self-hosted LangSmith. Requires the [Enterprise plan](https://www.langchain.com/pricing) with LangSmith Deployment enabled.

#### [Hybrid](hybrid.md)
LangChain-managed control plane with Agent Servers and their data plane in your infrastructure. Traces flow to LangSmith Cloud or self-hosted LangSmith.

#### [Standalone server](deploy-standalone-server.md)
Deploy Agent Server with Docker, Compose, or Kubernetes. Bring your own PostgreSQL, Redis, and LangSmith license; no control plane. Optional [LangSmith tracing](observability.md) to Cloud or a self-hosted instance.

## Common setups

* **Managed hosting for your agents.** LangSmith Deployment on [Cloud](deploy-to-cloud-overview.md). LangChain hosts the control plane, data plane, and databases. Pairs with LangSmith Cloud.
* **Agents in your VPC, control plane managed.** LangSmith Deployment via [Hybrid](hybrid.md). LangChain hosts the control plane; you host Agent Servers and their data plane. Pairs with LangSmith Cloud or self-hosted LangSmith.
* **Full data residency or air-gapped.** [Self-hosted LangSmith Deployment](deploy-with-control-plane.md). You host the control plane and Agent Servers in your own infrastructure alongside self-hosted LangSmith.
* **Agent runtime only, no control plane.** [Standalone Agent Server](deploy-standalone-server.md). Run Agent Server containers with Docker or Kubernetes without a control plane, optionally sending traces to LangSmith Cloud or self-hosted.

For where the LangSmith platform runs, see [Platform setup](platform-setup.md).

## After deployment

Once deployed, agents work with [Agent Server](assistants.md)'s execution model: **assistants** for configuration, **threads** for state, and **runs** for workloads. For capabilities, tutorials, server customization, and operations, see [Agent Server](develop-agents-overview.md).

#### [Update prompts and contexts without redeploying](prompt-context-hub.md)
Manage the prompts and versioned contexts your deployed agents pull at runtime, so you can change behavior without a full deploy.

#### [Interact with your deployment using RemoteGraph](use-remote-graph.md)
Call your deployed graph from client code as if it were a local compiled graph.

#### [Find and fix failures with Engine](engine-overview.md)
Once agents are in production, use LangSmith Engine to detect recurring failures in their traces, diagnose root causes, and resolve them.

## Full-stack web apps

Ship a LangChain.js agent and chat UI together as a single web app. The Vite example uses LangSmith Deployment as the agent backend behind a separate UI. Other examples embed the agent inside the web framework's route handlers and ship to the host platform.

#### [Full-stack web apps](deploy-frameworks-and-platforms.md)
Ship a LangChain.js chat app: embed the agent in Next.js, SvelteKit, Nuxt, Cloudflare Workers, or Deno Deploy (no Agent Server required), or pair LangSmith Deployment with a Vite + React UI.

<span>
> **Image:** [LangSmith](deployment.md)
</span>

<span>
> **Image:** [Next.js](deployment.md)
</span>

<span>
> **Image:** [SvelteKit](deployment.md)
</span>

<span>
> **Image:** [Nuxt](deployment.md)
</span>

<span>
> **Image:** [Cloudflare Workers](deployment.md)
</span>

<span>
> **Image:** [Deno Deploy](deployment.md)
</span>

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deployment.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
