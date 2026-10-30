---
title: "Set up the LLM Gateway"
description: "Set up the LLM Gateway for a team by adding provider keys, granting permission to call the gateway, issuing API keys, and setting governance policies."
source: "https://docs.langchain.com/langsmith/llm-gateway-admin-setup"
category: "docs"
tags: [docs, langsmith, llm-gateway-admin-setup]
---

# Set up the LLM Gateway

> Set up the LLM Gateway for a team by adding provider keys, granting permission to call the gateway, issuing API keys, and setting governance policies.

> [!NOTE]
>
> The LLM Gateway is in [beta](release-stages.md).

This page walks an admin through preparing the [LLM Gateway](llm-gateway.md) for a team: connecting providers, granting access, issuing API keys, and setting policies. Complete the following sections in order. Each one links to the page that covers its topic in full.

> [!TIP]
>
> Some users can start without this setup. A [Workspace Admin](rbac.md#workspace-admin) can already call the gateway, and can add a provider key from the Simulator's **Needs key** prompt. If you are the only user in your organization, go to [Send your first LLM Gateway request](llm-gateway-first-request.md) instead.

## Enable the gateway on self-hosted LangSmith

On self-hosted LangSmith, [enable the gateway in the Helm chart](llm-gateway-self-hosted.md) before the other steps. Skip this section on other deployments.

## Add provider keys

Adding a provider key requires [permission to manage secrets](rbac.md#workspace-roles) in that workspace.

The gateway calls each provider with a key stored as a secret in the workspace that the caller's API key belongs to. Add a key for each provider your team calls, in each workspace that calls it. The gateway does not fall back to organization secrets for these calls.

Skip this section if your team calls only [Gateway Credits](llm-gateway-credits.md) models, which need no provider key.

For the steps and the secret name each provider uses, see [Add a provider key](llm-gateway-provider-authentication.md#add-a-provider-key).

## Grant permission to call the gateway

An API key needs the `gateway:invoke` and `workspaces:read` permissions to call the gateway. On plans without workspace roles, every user has the Workspace Admin role, which includes both, so no action is needed.

On the Enterprise plan, the built-in Workspace Editor and Workspace Viewer roles include neither permission. As an [Organization Admin](rbac.md#organization-admin), create a [custom role](rbac.md#custom-roles) with both permissions and assign it to the users who call the gateway, or assign them the Workspace Admin role.

For more information, see [Grant permission to call the gateway](llm-gateway-authentication.md#grant-permission-to-call-the-gateway).

## Decide how developers get API keys

Each request authenticates with a workspace-scoped LangSmith API key. Developers can create their own personal access token (PAT), which carries their role, or the Simulator creates one for them. For shared agents or a company-wide rollout through mobile device management (MDM), you can create service keys instead.

For key types and scoping, see [Choose a key type](llm-gateway-authentication.md#choose-a-key-type). For coding agent rollouts, see [Set up coding agents](llm-gateway-coding-agents.md).

## Optional: Set policies

Creating policies requires the `organization:gateway:manage` permission, which Organization Admins and Organization Operators have by default. On self-hosted LangSmith earlier than application version 0.18.9 (Helm chart versions before 0.18.0-rc.22), it requires `organization:manage` instead.

Use the tabs on the **LLM Gateway** page to create any of these policy types:

* **[Spend limits](llm-gateway-spend-policies.md)**: Hard caps at the organization, workspace, API key, or user level. Your organization may already have a default limit on the **Cost Controls** tab.
* **[Rate limits](llm-gateway-rate-limit-policies.md)**: Request or token limits in a time window.
* **[Model access](llm-gateway-model-access-policies.md)**: Which models users can call.
* **[Header-based policies](llm-gateway-header-policies.md)**: Spend caps, rate limits, and model access scoped by a custom request header, such as a customer or team identifier.
* **[Data policies](llm-gateway-data-policy.md)**: Detect and redact PII and secrets before they reach the model, and control whether request and response bodies are traced.

On the Enterprise plan, creating, updating, and deleting policies is recorded in [audit logs](audit-logs.md).

## Send a test request

To confirm the setup, follow [Send your first LLM Gateway request](llm-gateway-first-request.md). It sends a request from the Simulator and from code, and shows its trace. Share the same page with developers as their starting guide.

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-admin-setup.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
