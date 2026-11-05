---
title: "LangSmith BYOC is now available on AWS, Azure, and Google Cloud"
description: "LangSmith BYOC now runs on AWS (GA), Azure and Google Cloud (Beta). Your traces, evals, and agent deployments stay in your cloud account while LangChain runs it."
source: "https://www.langchain.com/blog/langsmith-byoc-aws-gc-azure"
category: "blog"
published: "2026-11-03T22:06:00.000Z"
author: "LangChain Accounts"
tags: [blog, langsmith-byoc-aws-gc-azure]
---

# LangSmith BYOC is now available on AWS, Azure, and Google Cloud

[LangSmith Bring Your Own Cloud (BYOC)](../langsmith/byoc.md) now runs on [AWS](https://aws.amazon.com/) (GA), [Azure](https://azure.microsoft.com/) (Beta), and [Google Cloud](https://cloud.google.com/) (Beta). Your traces, evals, datasets, prompts, and agent deployments stay in your own cloud account, on the cloud you choose, and LangChain manages the data plane for you, from orchestration and scaling to platform updates.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aea276c7d6eab5f11a82317_byoc-architecture-azure-light.svg)

## How BYOC splits LangSmith

By splitting the control plane and data plane in two, BYOC provides greater flexibily to decide where agents run and where telemetry lives, without taking on the work of running LangSmith. LangChain runs the [control plane](../langsmith/byoc-architecture.md#control-plane-and-data-plane-model), which holds auth, org and workspace config, billing metadata, hashed API keys, and static UI assets. You own [the data plane](../langsmith/byoc-architecture.md#provisioned-resources), which holds everything sensitive, from traces, prompts, and datasets to experiments, agent deployments, and workspace secrets.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aea283e15ce584b626554b9_byoc-fig1-control-data-plane.svg)

‍

An organization can hold several data planes, each in its specific account and region, and each data plane holds its workspaces. This lets you split data planes by region, environment, or business unit.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aea4c5dc9940a62a467e47b_Create%20workspace%20byoc.png)

For example, a platform team might run production and staging data planes in separate AWS accounts, while a business unit that standardized on Azure runs its own, separate BYOC deployment on Azure. Each team's traces land in the account that team owns.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aea2886459b79e034d9a33c_byoc-org-hierarchy.svg)

## Why we built BYOC

Until now, teams with strict compliance boundaries deployed and maintained self-hosted LangSmith. This kept their data inside their own boundary, but it took dedicated platform engineers to patch stateful services, configure databases, and run schema migrations.

With BYOC, LangChain provisions and operates LangSmith inside your own virtual network. Consider a team running agent applications across several environments. With self-hosted, every update to the execution components meant coordinating downtime and managing custom Helm rollouts in each environment. With BYOC, the data in your data plane stays in your VPC while LangChain handles scaling, schema updates, and runtime dependencies.

While self-hosting continues to be a reliable deployment option for customers who require complete control, BYOC provides the best of both worlds for customers who need it.

### What AWS customers have seen

Since we launched BYOC on AWS in August, many teams have chosen to run LangSmith in their own cloud with BYOC. They point to three main benefits:

- **Continuous upgrades.** LangChain rolls out platform updates, so teams no longer plan maintenance windows or manage Helm upgrades.
- **The latest LangSmith features.** New features reach BYOC data planes soon after they ship on LangSmith Cloud, without waiting for the next self-hosted release.
- **Automatic scaling.** Services scale with load, so teams get consistent uptime and a smooth experience as usage grows.

By expanding LangSmith BYOC to Azure and Google Cloud, more teams can get access to this experience while choosing their preferred cloud vendor.

## What BYOC looks like on each cloud

Each cloud has its own network policies, identity model, and security requirements, so BYOC is built from each cloud's own building blocks. While built on each cloud’s building blocks, the core LangSmith experience is common across clouds and deployment options:

- Traces, trajectories, evaluations, and insights run on the data plane.
- [LLM Gateway](../langsmith/llm-gateway.md) is runs in the data plane with support for bringing your own provider keys.
- [LangSmith deployment](../langsmith/deployment.md) runs in your cluster.
- [Engine](../langsmith/engine.md) runs over your data on your own model providers.
- [Sandboxes](../langsmith/sandboxes.md) for isolation within your private cloud
- On all three clouds, BYOC data planes also run [Managed Deep Agents](../langsmith/python/managed-deep-agents-overview.md) endpoints.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aebb260e45ffe2b42dea5ce_image-no-azure.png)

**Azure:** BYOC runs the data plane inside a dedicated virtual network with a [private AKS API endpoint](https://learn.microsoft.com/en-us/azure/aks/private-clusters). We deploy [Istio](https://istio.io/latest/docs/) and [KEDA with Helm](https://keda.sh/docs/latest/deploy/) for ingress routing and event-driven scaling, and system telemetry goes to [Azure Monitor](https://learn.microsoft.com/en-us/azure/azure-monitor/).

![LangSmith Data Planes settings page listing two Azure BYOC data planes](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aea10dd672af68b149a7ffd_6aea10239315ae16d38add01_byoc-data-planes-azure.png)

**Google Cloud:** At launch, Google Cloud data planes can run in any region and are managed from LangSmith's US control plane. Resources use namespace-scoped names, so they don't collide with your existing infrastructure.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aea28ee1949407b97bdc5e9_Google%20BYOC.png)

**AWS:** BYOC runs inside your existing VPC, with the database in subnets you choose. Security teams can attach their own security groups to each application role, so the data plane fits the ingress and egress inspection policies you already run.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aea2906aef61fc4742bdb5c_byoc-AWS.svg)

## Move from self-hosted without starting over

Self-hosted LangSmith gave you full control of where your data lives, but required significant maintenance overhead. BYOC keeps the data in your account while we run the infrastructure, and you can bring your existing self-hosted data with you. Both deployment options run LangSmith reliably, and the choice depends on your specific needs.

The migration happens in two steps. Step 1 is provisioning the BYOC data plane. In step 2, workspace resources move using our open source [migration tool](https://github.com/langchain-ai/langsmith-data-migration-tool), which reads from your self-hosted instance but does not result in downtime or data changes on it. On every cloud, it covers users and roles, datasets, experiments, and prompts. It also brings over annotation queue config, automation rules, and dashboards.

Your traces, runs, and feedback move as a separate step that LangChain runs for you with internal tooling. Trace migration is available on AWS today.

![](https://cdn.prod.website-files.com/65c81e88c254bb0f97633a71/6aea291ac3ff3f8c7209ce7e_byoc-migration-flow.svg)

## Flexible, Open Platform

LangSmith gives you an open, flexible platform for building and running agents without vendor lock-in. You can build with open-source frameworks like [LangChain](https://www.langchain.com/langchain), [LangGraph](https://www.langchain.com/langgraph) and [Deep Agents](https://github.com/langchain-ai/deepagents), while retaining complete ownership of your data, models, and infrastructure. The [LLM Gateway](https://www.langchain.com/langsmith/llm-gateway) connects to 11 model providers out of the box, plus any OpenAI- or Anthropic-compatible endpoint. With this expansion, LangSmith BYOC runs across AWS, Azure, and Google Cloud, using public Terraform modules hosted at [github.com/langchain-ai/terraform](https://www.google.com/search?q=https%3A%2F%2Fgithub.com%2Flangchain-ai%2Fterraform) and an open-source migration tool.

## Get started

[Contact sales](https://www.langchain.com/contact-sales) to provision a BYOC data plane on AWS, Azure, or Google Cloud. The docs cover the [architecture](../langsmith/byoc-architecture.md), the [shared responsibility model](../langsmith/byoc-shared-responsibility.md), [migration](../langsmith/byoc-migration.md), [usage](../langsmith/byoc-usage.md), and common questions in the [FAQ](../langsmith/byoc-faq.md), with the Create Data Plane API in the [API reference](../langsmith/smith-api/data_planes/create-a-new-data-plane.md).
