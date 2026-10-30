---
title: "Rate limit policies"
description: "Limit the number of requests or tokens an organization, workspace, user, or API key can send through the LLM Gateway in a rolling time window."
source: "https://docs.langchain.com/langsmith/llm-gateway-rate-limit-policies"
category: "docs"
tags: [docs, langsmith, llm-gateway-rate-limit-policies]
---

# Rate limit policies

> Limit the number of requests or tokens an organization, workspace, user, or API key can send through the LLM Gateway in a rolling time window.

> [!NOTE]
>
> The LLM Gateway is in [beta](release-stages.md).

A rate limit policy restricts how many **requests** or **tokens** a subject can consume through the [LLM Gateway](llm-gateway.md) in a short rolling time window. The gateway enforces the limit in real time and blocks any request that would push the subject past it, returning a `429` response with a `Retry-After` header and a body that names the blocking policy:

```json
{"type":"error","error":{"message":"request blocked by gateway policies: <POLICY_NAME>"}}
```

The `Retry-After` value is the number of seconds until the current window resets. Clients should honor this header and back off before retrying.

A blocked request never reaches the provider, so it does not trigger a [fallback chain](llm-gateway-fallbacks.md), even though `429` is a default fallback trigger.

> [!TIP]
>
> Rate limit policies and [spend cap policies](llm-gateway-spend-policies.md) are complementary and can be applied together: spend caps for cost control, rate limits for throughput and traffic control.

## Policy dimensions

Rate limit policies are evaluated for every incoming request.

| Subject | What it limits | Example |
| - | - | - |
| **Organization** | Requests or tokens across all workspaces in the org | "The entire org cannot send more than 5,000 requests per minute" |
| **Workspace** | Requests or tokens within a single [workspace](administration-overview.md#workspaces) or group of workspaces | "The R\&D workspace cannot exceed 1,000,000 tokens per hour" |
| **User** | Requests or tokens from a single user or group of users (resolved from the API key's identity) | "No individual developer can send more than 100 requests per minute" |
| **API key** | Requests or tokens from a single [API key](create-account-api-key.md) or group of API keys | "The customer support agent keys share a limit of 200 requests per minute" |

### Defaults vs. granular policies

Rate limit policies have two modes:

1. **Default policies** apply automatically to every member of a subject dimension. Example: "Every user in this workspace gets a default cap of 100 requests per minute." There is no need to create a policy per person.
2. **Granular policies** target a named subject and override the default for that subject only. Example: "The on-call engineer gets 500 requests per minute." Editing the default updates everyone still on it.

### Independent enforcement

Each subject is tracked and enforced separately. One user hitting their limit does not affect other users.

## Limits

A single rate limit policy can enforce **multiple limits at once**. For example, one policy can enforce both 100 requests per minute and 1,000,000 tokens per hour simultaneously.

Each limit has three fields:

| Field | Allowed values |
| - | - |
| **Value** | A positive integer (the cap) |
| **Metric** | `requests` or `tokens` (total tokens as reported by the provider) |
| **Window** | `minute` or `hour` |

Rules:

* At least one limit is required per policy.
* You cannot have two limits with the same metric and window combination within one policy.

## Create a rate limit policy

> [!WARNING]
>
> Creating and managing policies requires `organization:gateway:manage` permission. Organization Admins and Organization Operators have it by default. For what each organization role can do, see [Organization roles](rbac.md#organization-roles).

1. Go to **LLM Gateway** and select **Rate limiting**.
2. Click **Create rate limit**.
3. Select the scope (organization, workspace, user, or API key).
4. Add one or more limits, each with a value, metric, and window.
5. Click **Create rate limit**.

Policies take effect immediately.

A rate limit policy can also carry a condition on a custom request header, so traffic from a single subject splits into separate limits by header value. Use this to give each end customer, tenant, or team its own throughput allowance under one API key. For more information, see [Header-based policies](llm-gateway-header-policies.md).

## See also

* [Spend policies](llm-gateway-spend-policies.md): set cost caps alongside rate limits.
* [Header-based policies](llm-gateway-header-policies.md): split a limit by a custom request header so each header value gets its own allowance.
* [Data policies](llm-gateway-data-policy.md): add data policies.

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-rate-limit-policies.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
