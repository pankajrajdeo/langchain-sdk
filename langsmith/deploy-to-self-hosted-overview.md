# Deploy to self-hosted
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/deploy-to-self-hosted-overview)
Run the LangSmith Deployment platform on your own infrastructure with full control over data, networking, and resources.

Self-hosted LangSmith Deployment runs the [Agent Server](https://docs.langchain.com/langsmith/agent-server), control plane, data plane, and supporting databases inside infrastructure that you operate.

LangChain ships the container images, Helm charts, and license; you provide the Kubernetes cluster (or Docker host), PostgreSQL, Redis, and the networking and observability tooling that fit your environment. Self-hosted is the best deployment option when you have data residency, regulatory constraints, custom networking, or air-gapped requirements.

> [!NOTE]
> Self-hosted deployments require an [Enterprise plan](https://www.langchain.com/pricing) and the LangSmith license key delivered with that plan. For a setup guide, see [Self-hosted LangSmith](https://docs.langchain.com/langsmith/self-hosted).

## Topologies

LangSmith supports three self-hosted topologies that trade off setup complexity against control-plane features. Reference pages for [platform features](https://docs.langchain.com/langsmith/self-hosted-platform-features), [Agent Server metrics](https://docs.langchain.com/langsmith/self-hosted-agent-server-metrics), and [diagnostics](https://docs.langchain.com/langsmith/diagnostics-self-hosted) apply to all three.

#### [Full self-hosted platform](https://docs.langchain.com/langsmith/deploy-with-control-plane)
The complete LangSmith platform—[control plane](https://docs.langchain.com/langsmith/control-plane) UI and APIs, [data plane](https://docs.langchain.com/langsmith/data-plane) listener, observability, evaluation, and agent deployment management. Best for teams that want the LangSmith product experience inside their own network.

#### [Hybrid](https://docs.langchain.com/langsmith/hybrid)
LangChain-hosted control plane with the data plane (Agent Servers and databases) in your infrastructure. Best when you want managed deployment workflows but need agent workloads and customer data to stay inside your VPC.

#### [Standalone server](https://docs.langchain.com/langsmith/deploy-standalone-server)
The lightest option—Agent Server containers (API + queue workers) with your own PostgreSQL and Redis. No control plane, no managed UI. Best for embedding the runtime into existing infrastructure or running air-gapped.

#### [Platform features](https://docs.langchain.com/langsmith/self-hosted-platform-features)
Reference for self-hosted-only platform behavior: custom Postgres and Redis, listeners, and resource customization.

#### [Agent Server metrics](https://docs.langchain.com/langsmith/self-hosted-agent-server-metrics)
Prometheus and Datadog export for Agent Server, including Deployment UI metrics and internal metrics.

#### [Diagnostics](https://docs.langchain.com/langsmith/diagnostics-self-hosted)
Collect logs, inspect state, and troubleshoot a self-hosted installation.

## Who manages what

Self-hosted shifts ownership of infrastructure operations from LangChain to your team, which provides flexibility and control over how you configure and operate is layer:

|                                           | **Who manages it** | **Where it runs**   |
| ----------------------------------------- | ------------------ | ------------------- |
| LangSmith platform (UI, APIs, datastores) | You                | Your infrastructure |
| Agent Server runtime                      | You                | Your infrastructure |
| PostgreSQL and Redis                      | You                | Your infrastructure |
| CI/CD for your apps                       | You                | Your CI environment |
| Upgrades, scaling, and backups            | You                | Your infrastructure |

In return, you can integrate with your own [Postgres](https://docs.langchain.com/langsmith/self-hosted-platform-features#custom-postgresql) and [Redis](https://docs.langchain.com/langsmith/self-hosted-platform-features#custom-redis), size [CPU and memory](https://docs.langchain.com/langsmith/self-hosted-platform-features#resource-customization) for your workload, and operate inside your existing network and observability stack. For the corresponding Cloud-managed model, see [Deploy to Cloud](https://docs.langchain.com/langsmith/deploy-to-cloud-overview).

## Next steps

#### [Pick a topology](https://docs.langchain.com/langsmith/deploy-standalone-server)
Compare standalone server, full platform, and hybrid to find the right fit.

#### [Install the full platform](https://docs.langchain.com/langsmith/deploy-self-hosted-full-platform)
Deploy LangSmith on Kubernetes with the control plane and data plane.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/deploy-to-self-hosted-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
