# API formats

> Use OpenAI Chat Completions, Anthropic Messages, or OpenAI Responses requests to call models across providers through the LLM Gateway.

The standard LLM Gateway API supports three request and response formats. Choose the format your application already uses, then call bring-your-own-key or Gateway Credits models through the same endpoint.

> [!NOTE]
> **Beta:** The LLM Gateway is in [beta](release-stages.md).

## Compare API formats

| API format              | Base URL                                 | Prompt endpoint          | Compatible client                          |
| ----------------------- | ---------------------------------------- | ------------------------ | ------------------------------------------ |
| OpenAI Chat Completions | `https://gateway.smith.langchain.com/v1` | `POST /chat/completions` | OpenAI-compatible Chat Completions clients |
| Anthropic Messages      | `https://gateway.smith.langchain.com`    | `POST /v1/messages`      | Anthropic Messages clients                 |
| OpenAI Responses        | `https://gateway.smith.langchain.com/v1` | `POST /responses`        | OpenAI-compatible Responses clients        |

All formats authenticate with a workspace-scoped LangSmith API key. Pass it as the provider API key or as an `Authorization: Bearer` token.

For bring-your-own-key models, set `model` to `<provider>/<model>`, such as `openai/gpt-5.4-mini`, `anthropic/claude-sonnet-4-6`, or `azure/<deployment-name>`. For Gateway Credits models, pass a supported model name, such as `moonshotai/kimi-k3`.

## Use Chat Completions

Point an OpenAI-compatible client at `https://gateway.smith.langchain.com/v1`. For the full request and response schema, see the [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat).

```bash
curl https://gateway.smith.langchain.com/v1/chat/completions \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"anthropic/claude-sonnet-4-6","messages":[{"role":"user","content":"Hello!"}]}'
```

```python
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://gateway.smith.langchain.com/v1",
    api_key=os.environ["LANGSMITH_API_KEY"],
)
response = client.chat.completions.create(
    model="anthropic/claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Hello!"}],
)
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://gateway.smith.langchain.com/v1",
  apiKey: process.env.LANGSMITH_API_KEY,
});
const response = await client.chat.completions.create({
  model: "anthropic/claude-sonnet-4-6",
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Use Messages

Point an Anthropic client at `https://gateway.smith.langchain.com`. For the full request and response schema, see the [Anthropic Messages API](https://docs.anthropic.com/en/api/messages).

```bash
curl https://gateway.smith.langchain.com/v1/messages \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"openai/gpt-5.4-mini","max_tokens":1024,"messages":[{"role":"user","content":"Hello!"}]}'
```

```python
import os

import anthropic

client = anthropic.Anthropic(
    base_url="https://gateway.smith.langchain.com",
    api_key=os.environ["LANGSMITH_API_KEY"],
)
message = client.messages.create(
    model="openai/gpt-5.4-mini",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
```

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: "https://gateway.smith.langchain.com",
  apiKey: process.env.LANGSMITH_API_KEY,
});
const message = await client.messages.create({
  model: "openai/gpt-5.4-mini",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
```

## Use Responses

Point an OpenAI-compatible client at `https://gateway.smith.langchain.com/v1`. For the full request and response schema, see the [OpenAI Responses API](https://platform.openai.com/docs/api-reference/responses).

```bash
curl https://gateway.smith.langchain.com/v1/responses \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"anthropic/claude-sonnet-4-6","input":"Hello!"}'
```

```python
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://gateway.smith.langchain.com/v1",
    api_key=os.environ["LANGSMITH_API_KEY"],
)
response = client.responses.create(
    model="anthropic/claude-sonnet-4-6",
    input="Hello!",
)
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://gateway.smith.langchain.com/v1",
  apiKey: process.env.LANGSMITH_API_KEY,
});
const response = await client.responses.create({
  model: "anthropic/claude-sonnet-4-6",
  input: "Hello!",
});
```

## Enable prompt caching

OpenAI models (Chat Completions and Responses) support implicit prompt caching automatically, no extra parameters are required.

Anthropic models and some older OpenAI models require explicit opt-in to prompt caching. Pass provider-specific fields in your request body when calling these models through any standard gateway endpoint.

> [!NOTE]
> Explicit caching support is a temporary measure while a gateway-level caching policy is being developed. The following fields are passed through to the upstream provider.

### Anthropic models

Include `prompt_cache_options` with a `ttl` value:

```bash
curl https://gateway.smith.langchain.com/v1/responses \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "anthropic/claude-opus-5",
      "input": "Hello!",
      "prompt_cache_options": {"ttl": "30m"}
    }'
```

```python
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://gateway.smith.langchain.com/v1",
    api_key=os.environ["LANGSMITH_API_KEY"],
)
response = client.responses.create(
    model="anthropic/claude-opus-5",
    input="Hello!",
    extra_body={"prompt_cache_options": {"ttl": "30m"}},
)
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://gateway.smith.langchain.com/v1",
  apiKey: process.env.LANGSMITH_API_KEY,
});
const response = await client.responses.create({
  model: "anthropic/claude-opus-5",
  input: "Hello!",
  // @ts-ignore — provider-specific field
  prompt_cache_options: { ttl: "30m" },
});
```

The same field works with the Chat Completions endpoint:

```bash
curl https://gateway.smith.langchain.com/v1/chat/completions \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "anthropic/claude-opus-5",
      "messages": [{"role": "user", "content": "Hello!"}],
      "prompt_cache_options": {"ttl": "30m"}
    }'
```

### Older OpenAI models

Some older OpenAI models support explicit cache control via `prompt_cache_retention`. Set it to `"in_memory"` for most models. For `gpt-5.5` specifically, use `"24h"`:

```bash
curl https://gateway.smith.langchain.com/v1/responses \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.4-mini",
      "input": "Hello!",
      "prompt_cache_retention": "in_memory"
    }'
```

```bash
curl https://gateway.smith.langchain.com/v1/responses \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "model": "openai/gpt-5.5",
      "input": "Hello!",
      "prompt_cache_retention": "24h"
    }'
```

For full `prompt_cache_retention` documentation, see the [OpenAI prompt caching guide](https://developers.openai.com/api/docs/guides/prompt-caching#prompt-cache-retention).

## Understand translation behavior

The endpoint determines the format your application sends and receives. The model ID determines the upstream provider.

* When the provider supports the selected format natively, the gateway preserves that format.
* Otherwise, the gateway translates the request into a format supported by the provider and translates the response back, including streaming responses.
* Translation can reject fields that cannot be represented in the target provider format. Use [Direct model access](llm-gateway-direct-model-access.md) when provider-native behavior is required.

Every request resolves the same Provider Secrets, policies, and tracing configuration regardless of format.

## List models

Call `GET /v1/models` to list models available from providers configured for the workspace and from [Gateway Credits](llm-gateway-credits.md). The gateway returns a single OpenAI-compatible list:

```bash
curl https://gateway.smith.langchain.com/v1/models \
    -H "Authorization: Bearer $LANGSMITH_API_KEY"
```

```json
{
  "object": "list",
  "data": [
    {"id": "openai/gpt-5.4-mini", "object": "model"},
    {"id": "fireworks/accounts/fireworks/models/glm-5p2", "object": "model"},
    {"id": "anthropic/claude-opus-5", "object": "model"},
    {"id": "moonshotai/kimi-k3", "object": "model"}
  ]
}
```

Bring-your-own-key model IDs use the form `<provider>/<model>`. Hosted models use the slug shown in the response. Pass either ID exactly as shown when making a call. A bring-your-own-key provider without a configured secret is omitted; hosted models do not require a provider secret.

## Use a regional gateway

Replace `gateway.smith.langchain.com` with the hostname for your LangSmith region:

| Region   | Gateway hostname                   |
| -------- | ---------------------------------- |
| GCP US   | `gateway.smith.langchain.com`      |
| GCP EU   | `eu.gateway.smith.langchain.com`   |
| GCP APAC | `apac.gateway.smith.langchain.com` |
| AWS US   | `aws.gateway.smith.langchain.com`  |

Keep the same path for the selected API format.

## Use a BYOC data plane

The LLM Gateway is also available on [BYOC](byoc.md), where it runs inside your data plane so model requests and their traces stay in your VPC. Replace the gateway hostname with your [data plane endpoint](byoc-usage.md#find-your-data-plane-endpoint) and prefix the path with `/gateway`:

| API format              | Base URL                               | Prompt endpoint          |
| ----------------------- | -------------------------------------- | ------------------------ |
| OpenAI Chat Completions | `https://<data_plane_host>/gateway/v1` | `POST /chat/completions` |
| Anthropic Messages      | `https://<data_plane_host>/gateway`    | `POST /v1/messages`      |
| OpenAI Responses        | `https://<data_plane_host>/gateway/v1` | `POST /responses`        |

Authenticate with an API key scoped to a workspace in that data plane. Pass it as an `Authorization: Bearer` token:

```bash
curl https://<data_plane_host>/gateway/v1/chat/completions \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{"model":"anthropic/claude-sonnet-4-6","messages":[{"role":"user","content":"Hello!"}]}'
```

```python
import os

from openai import OpenAI

client = OpenAI(
    base_url="https://<data_plane_host>/gateway/v1",
    api_key=os.environ["LANGSMITH_API_KEY"],
)
response = client.chat.completions.create(
    model="anthropic/claude-sonnet-4-6",
    messages=[{"role": "user", "content": "Hello!"}],
)
```

```typescript
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://<data_plane_host>/gateway/v1",
  apiKey: process.env.LANGSMITH_API_KEY,
});
const response = await client.chat.completions.create({
  model: "anthropic/claude-sonnet-4-6",
  messages: [{ role: "user", content: "Hello!" }],
});
```

Or pass it as the provider API key. For example, an Anthropic Messages request sends the key in the `X-Api-Key` header:

```bash
curl https://<data_plane_host>/gateway/v1/messages \
    -H "X-Api-Key: $LANGSMITH_API_KEY" \
    -H "Anthropic-Version: 2023-06-01" \
    -H "Content-Type: application/json" \
    -d '{"model":"openai/gpt-5.4-mini","max_tokens":1024,"messages":[{"role":"user","content":"Hello!"}]}'
```

```python
import os

import anthropic

client = anthropic.Anthropic(
    base_url="https://<data_plane_host>/gateway",
    api_key=os.environ["LANGSMITH_API_KEY"],
)
message = client.messages.create(
    model="openai/gpt-5.4-mini",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}],
)
```

```typescript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  baseURL: "https://<data_plane_host>/gateway",
  apiKey: process.env.LANGSMITH_API_KEY,
});
const message = await client.messages.create({
  model: "openai/gpt-5.4-mini",
  max_tokens: 1024,
  messages: [{ role: "user", content: "Hello!" }],
});
```

Provider secrets, model IDs, policies, and tracing behave the same as on Cloud.

> [!WARNING]
> Data planes are provisioned with a private endpoint by default, so you need private connectivity to reach the base URL, such as Tailscale, AWS PrivateLink, or VPC peering.

## Handle errors

| Status or symptom                                           | Meaning                                                                                                              |
| ----------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------- |
| `400 Bad Request`                                           | The request is malformed, the model ID is unavailable or incorrectly formatted, or the request cannot be translated. |
| `401 Unauthorized`                                          | The LangSmith API key is missing or invalid.                                                                         |
| `403 Forbidden`                                             | The key does not have the required gateway permissions.                                                              |
| `429 Too Many Requests`                                     | A gateway rate limit or an upstream provider rate limit was reached.                                                 |
| No models with a provider prefix appear in `GET /v1/models` | The provider may not be configured or may not have returned a model catalog.                                         |

For setup-specific resolutions, see the [Quickstart](llm-gateway-quickstart.md).

## See also

* [Quickstart](llm-gateway-quickstart.md): make your first request and view its trace.
* [Direct model access](llm-gateway-direct-model-access.md): bypass format translation and use provider-native APIs.
* [Model fallbacks](llm-gateway-fallbacks.md): retry requests against backup models.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-api-formats.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
