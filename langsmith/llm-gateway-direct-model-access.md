# Direct model access

> Access provider APIs directly through provider-specific LLM Gateway paths without using the gateway standardization layer.

> [!NOTE]
> **Beta:** The LLM Gateway is in [beta](release-stages.md).

Direct model access exposes each provider API through a provider-specific gateway path. The gateway still handles authentication, provider secrets, policies, and tracing, but it does not translate the request and response into another provider's API format.

Prefer [standard model access](llm-gateway-quickstart.md) for model calls across providers. Use direct model access when you want to access a provider's API directly, preserve its native request and response behavior, and avoid the gateway's standardization layer.

## Choose a provider path

Append a provider path to your regional gateway base URL:

| Provider         | Gateway path | Secret name                                            |
| ---------------- | ------------ | ------------------------------------------------------ |
| Anthropic        | `/anthropic` | `ANTHROPIC_API_KEY`                                    |
| AWS Bedrock      | `/bedrock`   | `AWS_BEARER_TOKEN_BEDROCK`                             |
| Azure Foundry    | `/azure`     | `AZURE_FOUNDRY_API_KEY`, `AZURE_FOUNDRY_RESOURCE_NAME` |
| Baseten          | `/baseten`   | `BASETEN_API_KEY`                                      |
| Fireworks        | `/fireworks` | `FIREWORKS_API_KEY`                                    |
| Google Gemini    | `/gemini`    | `GOOGLE_API_KEY`                                       |
| Google Vertex AI | `/vertex`    | `VERTEX_SERVICE_ACCOUNT_JSON`                          |
| OpenAI           | `/openai`    | `OPENAI_API_KEY`                                       |

[Gateway Credits models](llm-gateway-credits.md) use the standard endpoint rather than a provider-specific path. These hosted models require no provider secret of your own.

## Configure provider SDKs

Set each provider SDK's base URL to its direct gateway path and use your LangSmith API key as the provider API key:

```bash
export LANGSMITH_API_KEY="lsv2_..._....cbed3e"
export BASE_URL="https://gateway.smith.langchain.com"

export ANTHROPIC_BASE_URL="$BASE_URL/anthropic"
export OPENAI_BASE_URL="$BASE_URL/openai/v1"
export GOOGLE_GEMINI_BASE_URL="$BASE_URL/gemini"

export ANTHROPIC_API_KEY="$LANGSMITH_API_KEY"
export OPENAI_API_KEY="$LANGSMITH_API_KEY"
export GEMINI_API_KEY="$LANGSMITH_API_KEY"
export GOOGLE_API_KEY="$LANGSMITH_API_KEY"
```

The gateway resolves the actual provider key from your workspace's Provider Secrets, so the provider key does not need to be stored locally.

```python
import os

from openai import OpenAI

client = OpenAI(
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["LANGSMITH_API_KEY"],
)
response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": "ping"}],
)
print(response.choices[0].message.content)
```

```python
import os

import anthropic

client = anthropic.Anthropic(
    base_url=os.environ["ANTHROPIC_BASE_URL"],
    api_key=os.environ["LANGSMITH_API_KEY"],
)
message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=1024,
    messages=[{"role": "user", "content": "ping"}],
)
print(message.content[0].text)
```

Direct paths use the provider's native model name without a provider prefix.

## Configure LangChain and Deep Agents

[LangChain](../langchain/overview.md) chat models and [Deep Agents](../deepagents/overview.md), including [Deep Agents Code](../deepagents/code/overview.md), support direct gateway paths through a convenience environment variable:

```bash
export LANGSMITH_GATEWAY="true"
```

This routes supported chat models through their provider-specific paths at `https://gateway.smith.langchain.com`, using `LANGSMITH_API_KEY` for authentication. To use a regional gateway, set its URL instead of `true`:

```bash
export LANGSMITH_GATEWAY="https://eu.gateway.smith.langchain.com"
```

> [!NOTE]
> If you need to use a different API key for gateway calls than your default `LANGSMITH_API_KEY`, set `LANGSMITH_GATEWAY_API_KEY` as an override. It must be a workspace-scoped key with the `gateway:invoke` permission.

<details>
<summary>Supported models and configuration precedence</summary>

* Supported in Python only.
* Supported chat models:
  * [Anthropic](../integrations/chat/anthropic.md) (`langchain-anthropic >= 1.5.1`)
  * [Baseten](../integrations/chat/baseten.md) (`langchain-baseten >= 0.2.3`)
  * [Fireworks](../integrations/chat/fireworks.md) (`langchain-fireworks >= 1.5.1`)
  * [Google Gemini](../integrations/chat/google_generative_ai.md) (`langchain-google-genai >= 4.3.2`)
  * [OpenAI](../integrations/chat/openai.md) (`langchain-openai >= 1.4.1`)
* Provider-specific base URLs take precedence over the gateway setting. For example, `OPENAI_API_BASE` sends OpenAI to that URL while every other supported provider continues to use the gateway.

</details>

## Use a regional gateway

If your LangSmith account is on a regional instance, use the corresponding [regional gateway](llm-gateway-api-formats.md#use-a-regional-gateway) and append the provider path. For example, use `https://eu.gateway.smith.langchain.com/anthropic` for direct Anthropic access in GCP EU.

## See also

* [Quickstart](llm-gateway-quickstart.md): use the standard API to call models across providers.
* [Admin setup](llm-gateway-admin-setup.md): configure provider secrets and access.
* [Traces, Engine, and access control](llm-gateway-access.md): see where gateway traces appear and who can view them.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-direct-model-access.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
