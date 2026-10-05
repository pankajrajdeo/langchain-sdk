---
title: "Docs by LangChain: PRODUCTS AND SETUP LangSmith setup"
description: "Documentation for LangSmith, Fleet, and our open source packages."
source: "https://docs.langchain.com/_llms/products-and-setup/lang-smith-setup"
category: "docs"
tags: [docs, llms, products-and-setup, lang-smith-setup]
---

# Docs by LangChain: PRODUCTS AND SETUP LangSmith setup

> Documentation for LangSmith, Fleet, and our open source packages.

## LangSmith setup

### Overview

- [LangSmith setup](../../langsmith/langsmith-setup-overview.md): How a LangSmith workspace is organized, where LangSmith runs, and who can do what across your organization.

#### Hosting

- [Set up LangSmith](../../langsmith/platform-setup.md): Host and manage LangSmith infrastructure for observability, evaluation, and prompt engineering.

#### Agent-based workspaces

- [Agents](../../langsmith/agents.md): What an agent is in LangSmith, how a workspace organizes its agents, how environments divide an agent's traces, and how an identifier differs from a display name.
- [Agent environments](../../langsmith/agent-environments.md): How an agent's environments divide its traces, how to select one, and which parts of the set are fixed.
- [Navigate agents](../../langsmith/navigate-agents.md): How the agent switcher moves between the agent list and a single agent, which sections need an agent, and what the agent Overview shows.
- [Create an agent](../../langsmith/create-an-agent.md): The four ways an agent is created in LangSmith, what each route decides about the agent it makes, and the rules an identifier must follow.
- [Build an agent in the UI](../../langsmith/build-an-agent.md): How the Build tab configures an agent from a form, what each section of that form sets, and where the new agent's traces land.
- [Deploy to an agent environment](../../langsmith/deploy-to-agent-environment.md): How the LangGraph and Managed Deep Agents CLIs bind a deployment to an agent and an environment, which values each flag takes, and which CLI versions accept them.

### Account

- [Account](../../langsmith/admin.md): Set up your LangSmith account, including API keys, profile configuration, integrations, and pricing tiers.
- [Create an account and API key](../../langsmith/create-account-api-key.md)
- [Profile configuration](../../langsmith/profile-configuration.md): Configure LangSmith SDK credentials and endpoints with a local profile file.
- [Pricing plans](../../langsmith/pricing-plans.md)
- [LangSmith for Enterprise](../../langsmith/enterprise.md): Hosting options, access control, data privacy, cost controls, and security compliance for Enterprise users.

#### Billing & usage

- [Manage billing in your account](../../langsmith/billing.md)
- [View usage](../../langsmith/view-usage.md): What usage data is available in LangSmith, what each metric means, and what differs for Self-hosted.
- [Granular billable usage](../../langsmith/granular-usage.md): Retrieve detailed trace and LangSmith Deployment usage data broken down by workspace, project, user, or API key.

### Cloud

- [Cloud (SaaS)](../../langsmith/cloud.md)

#### Reference

- [LangSmith Cloud changelog](../../langsmith/changelog.md): Weekly updates to LangSmith Cloud
- [Release stages](../../langsmith/release-stages.md): How LangSmith labels features as alpha, beta, or generally available, and what each stage means for stability, support, and availability
- [API and SDK deprecation policy](../../langsmith/endpoint-deprecation.md): How LangSmith deprecates and removes API endpoints and SDK methods in cloud and self-hosted deployments.
- [Migrate to SmithDB-backed SDK methods](../../langsmith/smithdb-sdk-migration.md): Migrate your existing LangSmith SDK methods to their SmithDB-backed equivalents for faster agent observability.

### BYOC

- [Bring Your Own Cloud (BYOC)](../../langsmith/byoc.md): Deploy LangSmith services and store data in your own cloud environment while LangChain operates, scales, and upgrades the infrastructure.
- [Why BYOC](../../langsmith/byoc-why.md): Compare LangSmith BYOC with self-hosted LangSmith to decide which deployment model fits your organization.
- [BYOC architecture](../../langsmith/byoc-architecture.md): How a LangSmith BYOC deployment is structured across the LangChain control plane and the data plane in your AWS account.
- [BYOC shared responsibility model](../../langsmith/byoc-shared-responsibility.md): How LangChain and your organization divide responsibility for a LangSmith BYOC deployment across operations, security, support, and compliance.
- [BYOC onboarding](../../langsmith/byoc-onboarding.md): Set up a LangSmith BYOC data plane, from enabling BYOC on your organization to creating workspaces and connecting privately.
- [Bring your own VPC on AWS](../../langsmith/byoc-byovpc.md): Create a customer-managed VPC for LangSmith BYOC, configure a reduced-permission IAM role, and supply your VPC and subnet IDs.
- [Bring your own IAM roles (AWS)](../../langsmith/byoc-byoiam.md): Create customer-managed IAM roles for LangSmith BYOC, remove IAM management permissions from the provisioning role, and deploy with existing roles.
- [Migrate to BYOC](../../langsmith/byoc-migration.md): Copy users, datasets, prompts, experiments, Fleet resources, and other data from an existing LangSmith instance into a BYOC data plane.
- [BYOC usage](../../langsmith/byoc-usage.md): Route tracing and API traffic to a LangSmith BYOC data plane, including tracing to multiple endpoints and the path prefixes for each service.
- [BYOC operations](../../langsmith/byoc-operations.md): How LangChain upgrades, patches, and maintains a LangSmith BYOC data plane, and when maintenance requires a scheduled window.
- [BYOC billing](../../langsmith/byoc-billing.md): How LangSmith BYOC is billed across your AWS account and your LangSmith contract, which AWS services carry cost, and the account quotas to check before you deploy.
- [BYOC FAQ](../../langsmith/byoc-faq.md): Answers to common questions about LangSmith BYOC, covering data residency, access, setup, the data plane model, and ongoing operations.

### Self-hosted

- [Self-hosted LangSmith](../../langsmith/self-hosted.md)

#### Get started by cloud provider

- [Self-hosted LangSmith on AWS](../../langsmith/aws-self-hosted.md)
- [Self-hosted LangSmith on Azure](../../langsmith/azure-self-hosted.md)
- [Self-hosted LangSmith on GCP](../../langsmith/gcp-self-hosted.md)

#### Deploy with Terraform

- [Deploy LangSmith with Terraform](../../langsmith/self-host-terraform.md): Provision LangSmith self-hosted on AWS, Azure, or GCP using LangChain's production-ready Terraform modules.

##### AWS

- [Deploy LangSmith on AWS with Terraform](../../langsmith/self-host-terraform-aws-deploy.md): End-to-end walkthrough for provisioning LangSmith self-hosted on AWS EKS using the LangChain Terraform modules.
- [AWS Terraform architecture](../../langsmith/self-host-terraform-aws-architecture.md): Platform layers, services, IRSA roles, networking, and module dependencies for LangSmith self-hosted on AWS EKS.
- [AWS Terraform variables reference](../../langsmith/self-host-terraform-aws-variables.md): Complete reference of Terraform variables for LangSmith self-hosted on AWS EKS.
- [AWS Terraform quick reference](../../langsmith/self-host-terraform-aws-quick-reference.md): Make targets, Terraform commands, kubectl, AWS CLI, and Helm operations for LangSmith self-hosted on AWS EKS.
- [AWS Terraform troubleshooting](../../langsmith/self-host-terraform-aws-troubleshooting.md): Common issues, fixes, and diagnostic commands for LangSmith self-hosted on AWS EKS deployed with the LangChain Terraform modules.

##### GCP

- [Deploy LangSmith on GCP with Terraform](../../langsmith/self-host-terraform-gcp-deploy.md): End-to-end walkthrough for provisioning LangSmith self-hosted on GCP GKE using the LangChain Terraform modules.
- [GCP Terraform architecture](../../langsmith/self-host-terraform-gcp-architecture.md): Platform layers, services, Workload Identity, networking, and module dependencies for LangSmith self-hosted on GKE.
- [GCP Terraform variables reference](../../langsmith/self-host-terraform-gcp-variables.md): Complete reference of Terraform variables for LangSmith self-hosted on GCP GKE.
- [GCP Terraform quick reference](../../langsmith/self-host-terraform-gcp-quick-reference.md): Make targets, Terraform, kubectl, gcloud, and Helm commands for LangSmith self-hosted on GKE.
- [GCP Terraform troubleshooting](../../langsmith/self-host-terraform-gcp-troubleshooting.md): Common issues, fixes, and diagnostic commands for LangSmith self-hosted on GKE deployed with the LangChain Terraform modules.

##### Azure

- [Deploy LangSmith on Azure with Terraform](../../langsmith/self-host-terraform-azure-deploy.md): End-to-end walkthrough for provisioning LangSmith self-hosted on Azure AKS using the LangChain Terraform modules.
- [Azure Terraform architecture](../../langsmith/self-host-terraform-azure-architecture.md): Platform layers, services, Workload Identity, networking, ingress options, and module dependencies for LangSmith self-hosted on AKS.
- [Azure Terraform variables reference](../../langsmith/self-host-terraform-azure-variables.md): Complete reference of Terraform variables for LangSmith self-hosted on Azure AKS.
- [Azure Terraform quick reference](../../langsmith/self-host-terraform-azure-quick-reference.md): Make targets, Terraform, kubectl, Azure CLI, and Helm commands for LangSmith self-hosted on AKS.
- [Azure Terraform troubleshooting](../../langsmith/self-host-terraform-azure-troubleshooting.md): Common issues, fixes, and diagnostic commands for LangSmith self-hosted on Azure AKS deployed with the LangChain Terraform modules.

#### Setup guides

- [Minimum versions for self-hosting dependencies](../../langsmith/self-host-dependency-versions.md): Minimum supported versions for the databases, tools, and infrastructure required to self-host LangSmith.
- [Self-host LangSmith on Kubernetes](../../langsmith/kubernetes.md)
- [Enable additional LangSmith features](../../langsmith/deploy-self-hosted-full-platform.md): Enable LangSmith Deployment, Fleet, Insights, Chat, Sandboxes, and Engine on a self-hosted LangSmith instance.
- [Enable Engine](../../langsmith/engine-self-hosted-link.md)

##### Manage an installation

- [Interact with your self-hosted instance of LangSmith](../../langsmith/self-host-usage.md)
- [Upgrade an installation](../../langsmith/self-host-upgrades.md)
- [Disaster recovery for self-hosted LangSmith](../../langsmith/self-host-disaster-recovery.md)
- [Egress for billing and operational telemetry](../../langsmith/self-host-egress.md)
- [View trace counts across your organization](../../langsmith/self-host-organization-charts.md)
- [LangSmith-managed ClickHouse](../../langsmith/langsmith-managed-clickhouse.md)
- [Create an Ingress for installations (Kubernetes)](../../langsmith/self-host-ingress.md)
- [Mirror images for your LangSmith installation](../../langsmith/self-host-mirroring-images.md)
- [FIPS-compliant images](../../langsmith/self-host-fips.md): Run self-hosted LangSmith installation on FIPS 140 compliant container images

#### Configuration

- [Set up the LLM auth proxy](../../langsmith/llm-auth-proxy-self-hosted.md): Deploy an Envoy-based auth proxy that validates LangSmith-signed JWTs and routes LLM requests to your upstream provider or gateway.
- [Configure environment variables in the Helm chart](../../langsmith/self-host-environment-variables.md): How to use commonEnv and extraEnv to configure environment variables across LangSmith services in the Helm chart.
- [Configure LangSmith for scale](../../langsmith/self-host-scale.md)
- [Enable TTL and data retention](../../langsmith/self-host-ttl.md)
- [Use environment variables for model providers](../../langsmith/self-host-playground-environment-settings.md)
- [Customize the UI](../../langsmith/self-host-ui-customization.md): Customize your LangSmith self-hosted deployment.
- [Troubleshooting](../../langsmith/troubleshooting.md)

#### Connect external services

- [Enable blob storage](../../langsmith/self-host-blob-storage.md)
- [Connect to an external ClickHouse database](../../langsmith/self-host-external-clickhouse.md)
- [Connect to an external PostgreSQL database](../../langsmith/self-host-external-postgres.md)
- [Connect to an external Redis or Valkey database](../../langsmith/self-host-external-redis.md)
- [Connect self-hosted LangSmith to Slack](../../langsmith/self-host-slack.md): Configure your own Slack app for Engine and alert notifications on self-hosted LangSmith.

#### Platform auth & access control

- [Basic authentication with email and password](../../langsmith/self-host-basic-auth.md)
- [Set up SSO with OAuth2.0 and OIDC](../../langsmith/self-host-sso.md)
- [Customize user management](../../langsmith/self-host-user-management.md)
- [Configure custom TLS certificates](../../langsmith/self-host-custom-tls-certificates.md)
- [Use an existing secret for your installation (Kubernetes)](../../langsmith/self-host-using-an-existing-secret.md)

#### SmithDB

- [Enable SmithDB on self-hosted LangSmith](../../langsmith/self-host-smithdb.md): Run SmithDB alongside ClickHouse on a self-hosted LangSmith Kubernetes installation.
- [Install LangSmith with SmithDB](../../langsmith/self-host-smithdb-install.md): Enable SmithDB on a self-hosted LangSmith Kubernetes installation through staged Helm updates.
- [Prepare SmithDB supporting infrastructure](../../langsmith/self-host-smithdb-infrastructure.md): Provide a dedicated PostgreSQL metastore, object storage, and cache storage before enabling SmithDB.
- [Configure SmithDB for scale](../../langsmith/self-host-smithdb-scale.md): Choose tested SmithDB resource tiers and size Kubernetes workloads and the PostgreSQL metastore.
- [Configure SmithDB observability](../../langsmith/self-host-smithdb-observability.md): Scrape SmithDB application metrics and export logs and traces to your existing observability stack.
- [SmithDB metrics reference](../../langsmith/self-host-smithdb-metrics.md): Metrics to watch on each SmithDB component, what they measure, and how to read them.
- [Migrate ClickHouse history to SmithDB](../../langsmith/self-host-smithdb-migrate.md): Run the historical ClickHouse-to-SmithDB migration for a self-hosted LangSmith installation.
- [Troubleshoot SmithDB](../../langsmith/self-host-smithdb-troubleshooting.md): Diagnose SmithDB failures, gather troubleshooting context, or disable and reset a SmithDB deployment on self-hosted LangSmith.

#### Self-hosted observability

- [Export LangSmith telemetry to your observability backend](../../langsmith/export-backend.md)
- [Configure your collector for LangSmith telemetry](../../langsmith/langsmith-collector.md)
- [Deploy an observability stack for your LangSmith deployment](../../langsmith/observability-stack.md)
- [Install Mission Control](../../langsmith/self-hosted-mission-control.md): Install Mission Control, an in-cluster console for monitoring, configuring, and operating self-hosted LangSmith on Kubernetes.

#### Hybrid

- [Hybrid](../../langsmith/hybrid.md): A LangSmith Deployment setup where you self-host Agent Servers in your infrastructure and send traces to LangSmith Cloud or a self-hosted LangSmith instance.
- [Setup guide (legacy)](../../langsmith/hybrid-legacy.md): Legacy hybrid deployment model with a LangChain-managed control plane and a self-managed data plane.

#### Scripts

- [Delete workspaces](../../langsmith/script-delete-a-workspace.md)
- [Delete organizations](../../langsmith/script-delete-an-organization.md)
- [Delete traces](../../langsmith/script-delete-traces.md)
- [Generate ClickHouse stats](../../langsmith/script-generate-clickhouse-stats.md)
- [Generate query stats](../../langsmith/script-generate-query-stats.md)
- [Run support queries against PostgreSQL](../../langsmith/script-running-pg-support-queries.md)
- [Run support queries against ClickHouse](../../langsmith/script-running-ch-support-queries.md)

#### Reference

- [Self-hosted LangSmith changelog](../../langsmith/self-hosted-changelog.md)
- [Release policy](../../langsmith/release-versions.md): Release channels, cadence, and version support for self-hosted LangSmith.
- [API and SDK deprecation policy](../../langsmith/endpoint-deprecation.md): How LangSmith deprecates and removes API endpoints and SDK methods in cloud and self-hosted deployments.
- [Migrate to SmithDB-backed SDK methods](../../langsmith/smithdb-sdk-migration.md): Migrate your existing LangSmith SDK methods to their SmithDB-backed equivalents for faster agent observability.

### Govern

- [Govern](../../langsmith/govern-overview.md): Administer users, access control, organizational structure, and compliance policies for your LangSmith organization.

#### Organization

- [Overview](../../langsmith/administration-overview.md)
- [Manage your organization using the API](../../langsmith/manage-organization-by-api.md)
- [Manage LangSmith with Terraform](../../langsmith/manage-with-terraform.md): Use the official LangSmith Terraform provider to manage workspaces, access controls, resource tags, evaluators, run rules, and alert rules as code.

##### Workspace setup

- [Set up hierarchy](../../langsmith/set-up-hierarchy.md)
- [Workload isolation](../../langsmith/workload-isolation.md)
- [How agent-based workspaces differ](../../langsmith/migrate-to-agent-based-workspaces.md): What changes when a workspace moves from organizing traces by tracing project to organizing them by agent and environment.
- [Set up resource tags](../../langsmith/set-up-resource-tags.md): Create and manage resource tags to organize projects, datasets, prompts, and other resources within a LangSmith workspace.
- [Manage model configurations](../../langsmith/model-configurations.md): Manage model configurations and control their availability across LangSmith features.

#### Users & access control

- [User management](../../langsmith/user-management.md)
- [Role-based access control](../../langsmith/rbac.md)
- [Attribute-based access control](../../langsmith/abac.md)
- [Organization and workspace operations reference](../../langsmith/organization-workspace-operations.md)
- [Authentication methods](../../langsmith/authentication-methods.md)
- [Manage user access in SSO organizations](../../langsmith/jit-invite-sso.md)

#### Tools

- [LangSmith Chat](../../langsmith/chat.md): Use Chat in LangSmith to analyze traces, threads, prompts, and evaluations.
- [LangSmith CLI](../../langsmith/langsmith-cli.md): Query and manage LangSmith projects, traces, runs, datasets, evaluators, experiments, and threads from the terminal
- [LangSmith skills](../../langsmith/skills.md): Use Agent Skills to work with LangSmith traces, datasets, and evaluators from your coding agent.

#### Auditing

- [Audit logs](../../langsmith/audit-logs.md): Track and review administrative actions across your LangSmith organization for security, compliance, and operational visibility.

#### Data & compliance

- [LangSmith shared responsibility model](../../langsmith/shared-responsibility-model.md): Overview of how LangChain and customers share security responsibilities for the LangSmith platform.
- [Data storage and privacy](../../langsmith/data-storage-and-privacy.md)
- [Data purging for compliance](../../langsmith/data-purging-compliance.md)
- [Scalability & resilience](../../langsmith/scalability-and-resilience.md)

#### Additional resources

- [LangSmith status](../../langsmith/status.md)

##### FAQ

- [Frequently asked questions](../../langsmith/faq.md)
- [Regions FAQ](../../langsmith/regions-faq.md)
