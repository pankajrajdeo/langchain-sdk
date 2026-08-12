# LangSmith Deployment
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/deployment)
Deploy and manage agents with durable execution, real-time streaming, and horizontal scaling.

**LangSmith Deployment** is a workflow orchestration runtime purpose-built for agent workloads. It provides the managed infrastructure agents need to run reliably in production at scale, supporting the full lifecycle from local development to deployment.

> [!NOTE]
> This page covers how your **agents** run in production with **LangSmith Deployment**.
>
> Where you run LangSmith for observability, evaluation, and prompt engineering is separate; refer to [Platform setup](https://docs.langchain.com/langsmith/platform-setup) for details.

## Deployable products

LangSmith Deployment is framework-agnostic which means you can deploy agents built with:

#### [LangGraph (and LangChain)](https://docs.langchain.com/langsmith/deployment-quickstart)
Use the LangGraph CLI and app templates to deploy an application to LangSmith.

#### [Google ADK](https://docs.langchain.com/langsmith/deploy-google-adk)
Deploy Google Agent Development Kit (ADK) agent as a LangGraph with the `deployments-wrap-sdk` package.

#### [Other frameworks](https://docs.langchain.com/langsmith/deploy-other-frameworks)
Deploy Claude Agent SDK, Strands, CrewAI, AutoGen, and other agent frameworks with the Functional API or `deployments-wrap-sdk`.

#### [Looking to deploy Deep Agents?](https://docs.langchain.com/langsmith/python/managed-deep-agents-overview)
Use Managed Deep Agents: the managed runtime for deploying code-first Deep Agents.

## LangSmith Deployment environments

Pick an environment based on where you want the [control plane](https://docs.langchain.com/langsmith/control-plane) and [data plane](https://docs.langchain.com/langsmith/data-plane) (Agent Servers and their databases) to run. All infrastructure types use the same [Agent Server](https://docs.langchain.com/langsmith/agent-server) runtime.

#### [Cloud](https://docs.langchain.com/langsmith/deploy-to-cloud-overview)
Fully managed by LangChain on AWS and GCP. Create deployments from GitHub in the LangSmith UI or with [`langgraph deploy`](https://docs.langchain.com/langsmith/cli#deploy). Requires a [Plus plan or above](https://www.langchain.com/pricing).

#### [Self-hosted with control plane](https://docs.langchain.com/langsmith/deploy-with-control-plane)
Run the LangSmith Deployment control plane and Agent Servers in your own Kubernetes cluster, alongside self-hosted LangSmith. Requires the [Enterprise plan](https://www.langchain.com/pricing) with LangSmith Deployment enabled.

#### [Hybrid](https://docs.langchain.com/langsmith/hybrid)
LangChain-managed control plane with Agent Servers and their data plane in your infrastructure. Traces flow to LangSmith Cloud or self-hosted LangSmith.

#### [Standalone server](https://docs.langchain.com/langsmith/deploy-standalone-server)
Deploy Agent Server with Docker, Compose, or Kubernetes. Bring your own PostgreSQL, Redis, and LangSmith license; no control plane. Optional [LangSmith tracing](https://docs.langchain.com/langsmith/observability) to Cloud or a self-hosted instance.

## Common setups

* **Managed hosting for your agents.** LangSmith Deployment on [Cloud](https://docs.langchain.com/langsmith/deploy-to-cloud-overview). LangChain hosts the control plane, data plane, and databases. Pairs with LangSmith Cloud.
* **Agents in your VPC, control plane managed.** LangSmith Deployment via [Hybrid](https://docs.langchain.com/langsmith/hybrid). LangChain hosts the control plane; you host Agent Servers and their data plane. Pairs with LangSmith Cloud or self-hosted LangSmith.
* **Full data residency or air-gapped.** [Self-hosted LangSmith Deployment](https://docs.langchain.com/langsmith/deploy-with-control-plane). You host the control plane and Agent Servers in your own infrastructure alongside self-hosted LangSmith.
* **Agent runtime only, no control plane.** [Standalone Agent Server](https://docs.langchain.com/langsmith/deploy-standalone-server). Run Agent Server containers with Docker or Kubernetes without a control plane, optionally sending traces to LangSmith Cloud or self-hosted.

For where the LangSmith platform runs, see [Platform setup](https://docs.langchain.com/langsmith/platform-setup).

## After deployment

Once deployed, agents work with [Agent Server](https://docs.langchain.com/langsmith/assistants)'s execution model: **assistants** for configuration, **threads** for state, and **runs** for workloads. For capabilities, tutorials, server customization, and operations, see [Agent Server](https://docs.langchain.com/langsmith/develop-agents-overview).

#### [Update prompts and contexts without redeploying](https://docs.langchain.com/langsmith/prompt-context-hub)
Manage the prompts and versioned contexts your deployed agents pull at runtime, so you can change behavior without a full deploy.

#### [Interact with your deployment using RemoteGraph](https://docs.langchain.com/langsmith/use-remote-graph)
Call your deployed graph from client code as if it were a local compiled graph.

#### [Find and fix failures with Engine](https://docs.langchain.com/langsmith/engine-overview)
Once agents are in production, use LangSmith Engine to detect recurring failures in their traces, diagnose root causes, and resolve them.

## Full-stack web apps

Ship a LangChain.js agent and chat UI together as a single web app. The Vite example uses LangSmith Deployment as the agent backend behind a separate UI. Other examples embed the agent inside the web framework's route handlers and ship to the host platform.

#### [Full-stack web apps](https://docs.langchain.com/langsmith/deploy-frameworks-and-platforms)
Ship a LangChain.js chat app: embed the agent in Next.js, SvelteKit, Nuxt, Cloudflare Workers, or Deno Deploy (no Agent Server required), or pair LangSmith Deployment with a Vite + React UI.

<span>
> **Image:** [LangSmith](https://docs.langchain.com/langsmith/deployment)
</span>

<span>
> **Image:** [Next.js](https://docs.langchain.com/langsmith/deployment)
</span>

<span>
> **Image:** [SvelteKit](https://docs.langchain.com/langsmith/deployment)
</span>

<span>
> **Image:** [Nuxt](https://docs.langchain.com/langsmith/deployment)
</span>

<span>
> **Image:** [Cloudflare Workers](https://docs.langchain.com/langsmith/deployment)
</span>

<span>
> **Image:** [Deno Deploy](https://docs.langchain.com/langsmith/deployment)
</span>

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deployment.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
