---
title: "Self-hosted LangSmith"
description: "Run LangSmith in your own Kubernetes cluster, with Insights and Chat enabled by default and optional features such as Sandboxes, Engine, Fleet, LLM Gateway, and LangSmith Deployment."
source: "https://docs.langchain.com/langsmith/self-hosted"
category: "docs"
tags: [docs, langsmith, self-hosted]
---

# Self-hosted LangSmith

> Run LangSmith in your own Kubernetes cluster, with Insights and Chat enabled by default and optional features such as Sandboxes, Engine, Fleet, LLM Gateway, and LangSmith Deployment.

> [!NOTE]
>
> Self-hosted LangSmith is an add-on to the Enterprise plan designed for LangChain's largest, most security-conscious customers. For more details, refer to [Pricing](https://www.langchain.com/pricing). [Contact our sales team](https://www.langchain.com/contact-sales) if you want a license key to trial LangSmith in your environment.

Self-hosted LangSmith runs the LangSmith platform in your own infrastructure so that trace and operational data stay in your environment. The base installation includes [observability](observability.md), [evaluation](evaluation.md), [prompt engineering](prompt-context-hub.md#prompts), [Insights](insights.md), and [Chat](chat.md). You can add [Sandboxes](sandboxes.md), [Engine](engine.md), [Fleet](fleet/index.md), [LLM Gateway](llm-gateway.md), and [LangSmith Deployment](deployment.md) when your use case requires them.

## Features

| Feature | Availability | What setup requires |
| - | - | - |
| Observability, evaluation, and prompt engineering | Included | The [base installation](kubernetes.md). |
| [Insights](insights.md) and [Chat](chat.md) (formerly Polly) | Enabled by default in Helm chart version 0.15.1 or later | One encryption key per feature and model access. See [Configure Insights and Chat](self-host-insights-chat.md). |
| [Sandboxes](enable-self-hosted-sandboxes.md) | Optional | KVM-capable nodes and JuiceFS storage on EKS, GKE, or AKS. |
| [Engine](engine-self-hosted.md) | Optional | Sandboxes, a license with the Engine entitlement, and Helm chart version 0.16.0 or later. Air-gapped installations require Helm chart version 0.17.0 or later. |
| [Fleet](enable-self-hosted-fleet.md) | Optional | Fleet services in your cluster. Does not require LangSmith Deployment. |
| [LLM Gateway](llm-gateway-self-hosted.md) | Optional (beta) | Helm chart version 0.17.1 or later. The `agent-gateway` service needs access to PostgreSQL, Redis, and other LangSmith pods. |
| [LangSmith Deployment](enable-self-hosted-deployment.md) | Optional | KEDA, an ingress, and a control plane and data plane. To run Agent Servers without a control plane, see [standalone servers](deploy-standalone-server.md). |

## Architecture

A self-hosted LangSmith instance runs a set of application services backed by several storage services.

![LangSmith architecture showing services and datastores](https://mintcdn.com/langchain-5e9cc07a/rqYqeBEA_2oeiw17/langsmith/images/cloud-arch-light.png?fit=max\&auto=format\&n=rqYqeBEA_2oeiw17\&q=85\&s=0790cbdf4fe131c74d1e60bb120834e3)

To access the LangSmith UI and send API requests, expose the [LangSmith frontend](#services) service. Depending on your installation method, this can be a load balancer or a port exposed on the host machine.

For architecture patterns and best practices on each cloud provider, see the [AWS](aws-self-hosted.md), [GCP](gcp-self-hosted.md), and [Azure](azure-self-hosted.md) guides.

### Services

| Service | Description |
| - | - |
|  **LangSmith frontend** | The frontend uses Nginx to serve the LangSmith UI and route API requests to the other servers. This serves as the entrypoint for the application and is the only component that must be exposed to users. |
|  **LangSmith backend** | The backend is the main entrypoint for CRUD API requests and handles the majority of the business logic for the application. This includes handling requests from the frontend and SDK, preparing traces for ingestion, and supporting the hub API. |
|  **LangSmith queue** | The queue handles incoming traces and feedback to ensure that they are ingested and persisted into the traces and feedback datastore asynchronously, handling checks for data integrity and ensuring successful insert into the datastore, handling retries in situations such as database errors or the temporary inability to connect to the database. |
|  **LangSmith platform backend** | The platform backend is another critical service that primarily handles authentication, run ingestion, and other high-volume tasks. |
|  **LangSmith Playground** | The Playground is a service that handles forwarding requests to various LLM APIs to support the Playground feature. This can also be used to connect to your own custom model servers. |
|  **LangSmith ACE (Arbitrary Code Execution) backend** | The ACE backend is a service that handles executing arbitrary code in a secure environment. This is used to support running custom code within LangSmith. |

### Storage services

> [!NOTE]
>
> LangSmith bundles all storage services by default. You can configure it to use external versions of all storage services. For production, use external storage services.

| Service | Description |
| - | - |
|  **ClickHouse** | [ClickHouse](https://clickhouse.com/docs/en/intro) is a high-performance, column-oriented SQL database management system (DBMS) for online analytical processing (OLAP). LangSmith uses ClickHouse as the primary data store for traces and feedback (high-volume data). 💡 [Connect to external ClickHouse](self-host-external-clickhouse.md) |
|  **SmithDB** | SmithDB is an optional columnar datastore built for agent trace data: deeply nested spans, multi-modal content, and spans that stay open for hours. SmithDB is available on LangSmith 0.17 and later. 💡 [Enable SmithDB](self-host-smithdb.md) |
|  **PostgreSQL** | [PostgreSQL](https://www.postgresql.org/about/) is a powerful, open source object-relational database system that uses and extends the SQL language combined with many features that safely store and scale the most complicated data workloads. LangSmith uses PostgreSQL as the primary data store for transactional workloads and operational data (almost everything besides traces and feedback). 💡 [Connect to external PostgreSQL](self-host-external-postgres.md) - AWS RDS, GCP Cloud SQL, Azure Database |
|  **Redis / Valkey** | [Redis](https://github.com/redis/redis) is a powerful in-memory key-value database that persists on disk. By holding data in memory, Redis offers high performance for operations like caching. LangSmith uses Redis to back queuing and caching operations. [Valkey](https://valkey.io/) is also officially supported as a drop-in replacement for Redis. 💡 [Connect to external Redis or Valkey](self-host-external-redis.md) - AWS ElastiCache, GCP Memorystore, Azure Cache |
|  **Blob storage** | LangSmith supports several blob storage providers, including [AWS S3](https://aws.amazon.com/s3/), [Azure Blob Storage](https://azure.microsoft.com/en-us/services/storage/blobs/), and [Google Cloud Storage](https://cloud.google.com/storage). LangSmith uses blob storage to store large files, such as trace artifacts, feedback attachments, and other large data objects. Blob storage is optional, but highly recommended for production deployments. 💡 [Enable blob storage](self-host-blob-storage.md) - AWS S3, GCP GCS, Azure Blob |

## Installation procedures

This page is an overview. The installation itself happens in the [Kubernetes installation guide](kubernetes.md), and optional features have their own setup guides.

To go from this page to a running instance:

**1. Install the base platform**

Follow [Self-host LangSmith on Kubernetes](kubernetes.md) from start to finish. It covers prerequisites, Helm configuration, Insights and Chat encryption keys, deployment, and verification. When you complete it, you'll have a running LangSmith instance with observability, evaluation, prompt engineering, Insights, and Chat.

Before you start, review the [minimum versions for self-hosting dependencies](self-host-dependency-versions.md). To provision the cluster, datastores, and Helm release together, use [Deploy with Terraform](self-host-terraform.md) instead of the Helm-only guide.

**2. (Optional) Add features**

After the base platform is running, enable the optional features your use case requires from the [Features](#features) table. See [Configure additional self-hosted features](self-host-additional-features.md). Skip this step if the base installation covers your use case.

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/self-hosted.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
