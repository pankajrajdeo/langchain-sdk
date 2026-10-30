---
title: "Custom model configurations"
description: "Call saved model configurations through the LLM Gateway to reach custom endpoints and use them in fallback chains."
source: "https://docs.langchain.com/langsmith/llm-gateway-model-configurations"
category: "docs"
tags: [docs, langsmith, llm-gateway-model-configurations]
---

# Custom model configurations

> Call saved model configurations through the LLM Gateway to reach custom endpoints and use them in fallback chains.

> [!NOTE]
>
> The LLM Gateway is in [beta](release-stages.md).

[Model configurations](model-configurations.md) are named, reusable definitions that pair a provider and model with credentials and settings. The LLM Gateway can route a request through a saved configuration when you set the model ID to `custom/<name>`. Use a configuration to reach an endpoint that a provider-prefixed model ID cannot address, such as a custom OpenAI-compatible endpoint.

## Understand what the gateway uses

A bring-your-own-key gateway call normally targets a model with a provider-prefixed ID such as `openai/gpt-5.4-mini`. When the model ID is `custom/<name>`, the gateway reads the following from the saved configuration instead:

* **Provider and model**: The gateway sends the configuration's model name upstream, replacing the `custom/<name>` value in the request body.
* **API key secret**: The gateway authenticates to the provider with the workspace secret named in the configuration.
* **Connection settings**: The base URL, the OpenAI provider API (Chat Completions or Responses), the Vertex AI project and location, and the **Preferred Bedrock Endpoint** for Amazon Bedrock, where the provider uses them. Only the gateway reads the Bedrock endpoint setting.

The gateway ignores generation parameters saved on the configuration, such as temperature, top P, and max output tokens. Pass these in each API request instead.

Workspace admins create configurations under **Settings** > **Model configurations**, and organization admins create [organization-scoped configurations](model-configurations.md#organization-scoped-model-configurations). For the steps, see [Create a configuration](model-configurations.md#create-a-configuration).

## Choose a configuration type

The gateway can call configurations for these providers:

* **Custom endpoints**: OpenAI-compatible, Anthropic-compatible, and [TypeSafe-compatible](compatible-decision-model-provider.md) endpoints.
* **Built-in providers**: Anthropic, Amazon Bedrock, Fireworks, Gemini Enterprise Agent Platform, Google Gemini, OpenAI, TypeSafe, and xAI.

A configuration for any other provider returns an error. Each custom endpoint type treats its URL differently:

* **OpenAI-compatible**: the base URL is the API root. The gateway appends the request path, such as `/chat/completions`, without adding `/v1`, so include `/v1` in the base URL if the server expects it.
* **Anthropic-compatible**: the gateway sends requests to the URL exactly as entered, so enter the full Messages endpoint, such as `https://example.com/v1/messages`. Only Messages requests are supported.
* **TypeSafe-compatible**: the gateway appends `/v1/systemone` unless you clear **Append /v1/systemone**, in which case it uses the URL exactly as entered.

## Call a configuration through the gateway

Use `custom/<name>` as the model ID in any standard gateway request, replacing `<name>` with the configuration's exact name as shown in **Settings** > **Model configurations**:

**Cloud**

```bash
curl https://gateway.smith.langchain.com/v1/responses \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"custom/my-openai-config","input":"Hello!"}'
```

**BYOC**

```bash
curl https://<data_plane_host>/gateway/v1/responses \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"custom/my-openai-config","input":"Hello!"}'
```

The gateway looks up the configuration by name in the API key's workspace, including [organization-scoped configurations](model-configurations.md#organization-scoped-model-configurations), routes the request to the configured provider and endpoint, and returns the response in the [API format](llm-gateway-api-formats.md) the client used. When a workspace configuration and an organization-scoped configuration share a name, the gateway uses the workspace configuration.

The gateway does not check the [Feature Access](model-configurations.md#feature-access) table, so an organization-scoped configuration is callable without enabling it in the workspace. It also ignores [OAuth client credentials](model-configurations.md#oauth-client-credentials) saved on a configuration and authenticates with the configuration's API key secret.

Saved configurations do not appear in the `GET /v1/models` list, so share configuration names with developers directly.

If a [model access policy](llm-gateway-model-access-policies.md#allow-saved-model-configurations) applies to the request, the policy must allow saved model configurations, or the gateway returns a `403` response.

A saved configuration can also be the primary model or a backup model in a fallback chain. For the steps, including how to give a Playground prompt its own fallback behavior, see [Model fallbacks](llm-gateway-fallbacks.md).

## See also

* [Manage model configurations](model-configurations.md): create, edit, and delete configurations; configure OAuth client credentials; manage organization-scoped configurations.
* [Model fallbacks](llm-gateway-fallbacks.md): retry failed requests against backup models and configurations.
* [API formats](llm-gateway-api-formats.md): supported request and response formats, model ID syntax, and translation behavior.

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-model-configurations.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
