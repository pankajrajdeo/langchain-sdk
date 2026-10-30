---
title: "LLM Gateway"
description: "Access models across providers with one LangSmith API key while tracing calls and enforcing spend and data protection policies."
source: "https://docs.langchain.com/langsmith/llm-gateway"
category: "docs"
tags: [docs, langsmith, llm-gateway]
---

# LLM Gateway

> Access models across providers with one LangSmith API key while tracing calls and enforcing spend and data protection policies.

> [!NOTE]
>
> The LLM Gateway is in [beta](release-stages.md).

The LLM Gateway is a proxy between your application and the model providers your workspace has configured. Your application authenticates with a [LangSmith API key](create-account-api-key.md). The gateway routes each request to the provider named in its model ID, traces the call, and applies your organization's governance policies.

Without the gateway, provider keys are copied onto every application and deployment that calls a model. Spend and data controls depend on each provider account. With the gateway, provider keys stay in LangSmith, every call appears as a [LangSmith trace](llm-gateway-traces.md), and [spend limits](llm-gateway-spend-policies.md), [rate limits](llm-gateway-rate-limit-policies.md), and [data policies](llm-gateway-data-policy.md) apply to every call in their scope.

## Choose a request format

The gateway accepts OpenAI Chat Completions, Anthropic Messages, and OpenAI Responses requests. The request format and the provider are independent: a Chat Completions request can call an Anthropic model, and the gateway translates the request and response when the provider uses a different native format. Keep the format your application already uses, and switch providers by changing the model ID. For endpoints, model ID syntax, and translation behavior, see [API formats](llm-gateway-api-formats.md).

LangChain chat models and Deep Agents reach the gateway through the `LANGSMITH_GATEWAY` environment variable, which uses [direct model access](llm-gateway-direct-model-access.md) in each provider's native format, so no translation applies.

## Choose how credentials are managed

The gateway calls each provider with a credential that LangSmith holds: your own provider key, stored as a workspace secret, or [Gateway Credits](llm-gateway-credits.md), which LangChain bills to your LangSmith account. For every credential source and who bills it, see [Provider authentication](llm-gateway-provider-authentication.md#choose-a-credential-source).

## Next steps

Start with the guide for your role:

> **[Set up the gateway for your team](llm-gateway-admin-setup.md)**
>
> Complete the initial setup to route requests through the gateway.

> **[Send your first request](llm-gateway-first-request.md)**
>
> Send a request from the Simulator, call the gateway from your code, and view the trace.

For further questions, contact [LangChain support](https://support.langchain.com).

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
