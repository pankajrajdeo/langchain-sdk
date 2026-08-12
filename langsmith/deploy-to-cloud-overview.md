# Deploy to Cloud
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/deploy-to-cloud-overview)
Deploy LangSmith agents to LangChain-managed Cloud infrastructure on AWS and GCP.

[LangSmith Cloud](https://docs.langchain.com/langsmith/cloud) is a **managed platform for deploying your agents**. LangChain hosts and operates the [control plane](https://docs.langchain.com/langsmith/control-plane), [data plane](https://docs.langchain.com/langsmith/data-plane), [Agent Server](https://docs.langchain.com/langsmith/agent-server) runtime, and supporting databases on AWS and GCP. Push code to a connected GitHub repository or invoke the `langgraph deploy` CLI, and the platform handles build, provisioning, scaling, and ongoing operations. Deployments come in two types: Serverless, a lightweight, fully managed option that scales to zero after a period of inactivity, and Dedicated, always-on infrastructure for production workloads. For details, see [Deployment types](https://docs.langchain.com/langsmith/cloud-platform-features#deployment-types).

> [!NOTE]
> Agent deployments running on Cloud require a [Plus plan or above](https://www.langchain.com/pricing). Before creating your first agent deployment, verify that your application runs locally with `langgraph dev`. Refer to [Local development and testing](https://docs.langchain.com/langsmith/local-dev-testing).

#### [Deploy on Cloud](https://docs.langchain.com/langsmith/deploy-to-cloud)
Step-by-step setup guide for creating, configuring, and managing Cloud deployments from the LangSmith UI or the `langgraph deploy` CLI.

#### [Cloud platform features](https://docs.langchain.com/langsmith/cloud-platform-features)
Reference for Cloud-only platform behavior: data regions, static IPs, payload limits, deployment types, and managed database provisioning.

#### [Quickstart](https://docs.langchain.com/langsmith/deployment-quickstart)
Deploy your first LangGraph application to Cloud in a few minutes.

To deploy a code-first Deep Agent without standing up your own Agent Server, [Managed Deep Agents](https://docs.langchain.com/langsmith/python/managed-deep-agents-overview) offers a CLI-first managed runtime in private beta.

## Next steps

#### [Run the quickstart](https://docs.langchain.com/langsmith/deployment-quickstart)
Deploy a starter LangGraph application end-to-end.

#### [Read the full deploy guide](https://docs.langchain.com/langsmith/deploy-to-cloud)
Configure environment variables, secrets, revisions, and deployment settings.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-to-cloud-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
