# Agent Server

> Configure and operate the LangSmith Agent Server runtime, including capabilities, application structure, auth, and customization.

Configure and build applications on the [Agent Server](https://docs.langchain.com/langsmith/agent-server) runtime. Once deployed, agents work with three primitives: [**assistants**](https://docs.langchain.com/langsmith/assistants) for configuration, [**threads**](https://docs.langchain.com/langsmith/use-threads) for state, and [**runs**](https://docs.langchain.com/langsmith/runs) for workloads. The pages in this tab cover the capabilities Agent Server provides, how to [structure your application](https://docs.langchain.com/langsmith/application-structure), and how to [secure](https://docs.langchain.com/langsmith/auth) and [customize](https://docs.langchain.com/langsmith/custom-routes) the server.

## Capabilities

#### [Develop your application](https://docs.langchain.com/langsmith/application-structure)
Structure your app, configure dependencies for Python, JavaScript, and monorepos, and connect agents with RemoteGraph, semantic search, TTLs, and CI/CD.

#### [Agent Server runtime](https://docs.langchain.com/langsmith/agent-server)
Work with assistants, threads, runs, and cron jobs. Stream to users, pause for human review, handle concurrent input, and connect via MCP and A2A.

#### [Auth & access control](https://docs.langchain.com/langsmith/auth)
Authenticate users, enforce resource-level access, and connect external OAuth2 identity providers.

#### [Server customization](https://docs.langchain.com/langsmith/caching)
Add caching, custom stores and checkpointers, lifespan hooks, middleware, custom routes, encryption, and configurable headers and logs.

## Tutorials

* [Collect user feedback for Agent Server runs](https://docs.langchain.com/langsmith/agent-server-feedback): Attach end-user feedback to runs and traces
* [Deploy other frameworks (e.g., Strands, CrewAI)](https://docs.langchain.com/langsmith/deploy-other-frameworks): Wrap existing agents with Functional API and deploy
* [Implement generative user interfaces with LangGraph](https://docs.langchain.com/langsmith/generative-ui-react): Stream UI elements to a React client
* [Implement a CI/CD pipeline](https://docs.langchain.com/langsmith/cicd-pipeline-example): Automate tests, evaluations, and deployments with GitHub Actions

## Securing and customizing your server

* [Custom auth](https://docs.langchain.com/langsmith/auth): Authentication and multi-tenant access control
* [Server customization](https://docs.langchain.com/langsmith/custom-routes): Custom routes, [middleware](https://docs.langchain.com/langsmith/custom-middleware), [lifespan hooks](https://docs.langchain.com/langsmith/custom-lifespan), [encryption](https://docs.langchain.com/langsmith/encryption)

## Operations

* [CI/CD pipelines](https://docs.langchain.com/langsmith/cicd-pipeline-example)
* [TTL configuration](https://docs.langchain.com/langsmith/configure-ttl) for state and thread management
* [Semantic search](https://docs.langchain.com/langsmith/semantic-search)

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/agent-server-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
