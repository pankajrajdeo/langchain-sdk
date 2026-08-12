# Deploy LangSmith with Terraform
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/self-host-terraform)
Provision LangSmith self-hosted on AWS, Azure, or GCP using LangChain's production-ready Terraform modules.

> [!NOTE]
> Self-hosted LangSmith is an add-on to the Enterprise plan designed for LangChain's largest, most security-conscious customers. See [pricing](https://www.langchain.com/pricing) for details, or [contact sales](https://www.langchain.com/contact-sales) to request a license key for trial.

LangChain publishes production-ready Terraform modules for [LangSmith self-hosted](https://docs.langchain.com/langsmith/self-hosted) at [github.com/langchain-ai/terraform](https://github.com/langchain-ai/terraform). The modules provision the cloud foundation (network, cluster, database, cache, object storage, secrets, DNS) and install the LangSmith Helm chart with sensible defaults.

Use this path when you want infrastructure as code from day one. If you already manage cloud infrastructure with your own tooling and need just the application install, follow the [Helm installation guide](https://docs.langchain.com/langsmith/kubernetes) instead.

> [!TIP]
> **Prefer Helm?** The [Kubernetes setup guide](https://docs.langchain.com/langsmith/kubernetes) walks through installing with Helm against any conformant cluster, no Terraform required. The Terraform path bundles cluster provisioning, secrets wiring, and the Helm release into one workflow.

## Choose a provider

#### [AWS (EKS)](https://docs.langchain.com/langsmith/self-host-terraform-aws-deploy)
Provision EKS, RDS PostgreSQL, ElastiCache, S3, and networking.

#### [Azure (AKS)](https://docs.langchain.com/langsmith/self-host-terraform-azure-deploy)
Provision AKS, Azure Database for PostgreSQL, Azure Managed Redis, Blob Storage, and Key Vault.

#### [GCP (GKE)](https://docs.langchain.com/langsmith/self-host-terraform-gcp-deploy)
Provision GKE, Cloud SQL, Memorystore, GCS, and Workload Identity.

## Prerequisites

Install the following tools before running the modules:

| Tool        | Version | Purpose                                          |
| ----------- | ------- | ------------------------------------------------ |
| `terraform` | 1.5     | Run the modules                                  |
| `kubectl`   | 1.33    | Inspect the cluster after provisioning           |
| `helm`      | 3.12    | Manage the LangSmith chart release               |
| Cloud CLI   | latest  | `aws`, `az`, or `gcloud` for the target provider |

You also need:

* A LangSmith license key. [Contact sales](https://www.langchain.com/contact-sales) to request one.
* Permissions in the target cloud account to create VPC or VNet networking, a managed Kubernetes cluster, managed databases, object storage, secrets, and IAM roles.
* A registered domain (or subdomain) for the LangSmith UI endpoint.

## Deployment tiers

Pick a tier with a single Terraform variable. The modules size every dependent resource accordingly.

| Tier               | PostgreSQL                                     | Redis                                                 | ClickHouse                                                              | Use case                             |
| ------------------ | ---------------------------------------------- | ----------------------------------------------------- | ----------------------------------------------------------------------- | ------------------------------------ |
| `dev`              | In-cluster                                     | In-cluster                                            | In-cluster                                                              | Demos, evaluations, short-lived POCs |
| `production`       | Cloud-managed (RDS, Cloud SQL, Azure Database) | Cloud-managed (ElastiCache, Memorystore, Azure Cache) | [LangChain Managed ClickHouse](https://docs.langchain.com/langsmith/langsmith-managed-clickhouse) | Persistent, scalable production      |
| `production-large` | Cloud-managed, larger instance class           | Cloud-managed, larger instance class                  | LangChain Managed ClickHouse                                            | High-throughput production           |

> [!WARNING]
> Use in-cluster ClickHouse for development and POC, not production. Production deployments must use [LangChain Managed ClickHouse](https://docs.langchain.com/langsmith/langsmith-managed-clickhouse) or a self-managed external ClickHouse cluster. Blob storage is always required because trace payloads must not live in ClickHouse.

## What the modules provision

* **Networking:** VPC or VNet with public and private subnets, NAT, and security groups.
* **Compute:** Managed Kubernetes (EKS, AKS, or GKE) with autoscaling node pools sized per tier.
* **Data plane:** Managed PostgreSQL, managed Redis or cache, and a blob storage bucket for trace payloads.
* **Secrets:** Cloud-native secret store (AWS SSM Parameter Store, Azure Key Vault, GCP Secret Manager) synced into Kubernetes by [External Secrets Operator](https://external-secrets.io/).
* **Ingress:** Cloud-native load balancer by default. Envoy Gateway (Gateway API) is available for multi-namespace dataplane deployments.
* **Optional hardening (AWS today):** AWS Network Firewall with FQDN egress allowlists, WAFv2, CloudTrail, and a private EKS API endpoint with SSM bastion access.

## Enterprise feature toggles

Each module exposes flags for the optional LangSmith add-ons. Toggle each in the `tfvars` file before running `make apply`.

* **[LangSmith Deployment](https://docs.langchain.com/langsmith/deploy-self-hosted-full-platform)** (`enable_deployments`): Agent Server plus the host-backend, listener, and operator that run and manage deployed agents.
* **[Fleet](https://docs.langchain.com/langsmith/fleet)** (`enable_fleet`): The agent-building product, formerly Agent Builder, deployed as a standalone service (chart v0.15+).
* **Insights** (`enable_insights`): ClickHouse-backed analytics.
* **Polly** (`enable_polly`): AI evaluation and monitoring.

## Next steps

* Pick a provider above and follow the deployment guide.
* Review [required dependency versions](https://docs.langchain.com/langsmith/self-host-dependency-versions) for PostgreSQL, ClickHouse, Redis, and Kubernetes.
* Plan capacity with the [scaling guide](https://docs.langchain.com/langsmith/self-host-scale).
* After the application is running, enable [LangSmith Deployment](https://docs.langchain.com/langsmith/deploy-self-hosted-full-platform) to add agent deployment and management to the UI.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-host-terraform.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
