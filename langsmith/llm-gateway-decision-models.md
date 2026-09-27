---
title: "Decision models"
description: "Use SemIf through the LangSmith LLM Gateway for structured classification and scoring with the System One API."
source: "https://docs.langchain.com/langsmith/llm-gateway-decision-models"
category: "docs"
tags: [docs, langsmith, llm-gateway-decision-models]
---

# Decision models

> Use SemIf through the LangSmith LLM Gateway for structured classification and scoring with the System One API.

Decision models classify or score text and return structured answers instead of generated chat messages. Call them through the [LLM Gateway](llm-gateway.md) with the System One API.

LangSmith provides an open source decision model, SemIf (`semif-qwen3.5-4b`), through the gateway for free through September 28, 2026.

> [!NOTE]
> SemIf is enabled for US organizations on Free, Developer, and Plus plans.

## Quickstart

Set your [LangSmith API key](create-account-api-key.md):

```bash
export LANGSMITH_API_KEY="<your-api-key>"
```

Then run a request:

#### Python
Install the TypeSafe SDK:

```bash
pip install typesafe-sdk
```

```python
import os

from typesafe_sdk import Noul, TypeSafeClient

client = TypeSafeClient(
    api_key=os.environ["LANGSMITH_API_KEY"],
    base_url="https://gateway.smith.langchain.com",
)

response = client.system_one(
    state="Hello!",
    model="semif-qwen3.5-4b",
    questions={
        "is_helpful": Noul(
            instructions="Does this explain what an LLM gateway does?"
        ),
    },
)
```

#### JavaScript
Install the TypeSafe SDK:

```bash
npm install @typesafe-ai/sdk
```

```javascript
import { noul, TypeSafeClient } from "@typesafe-ai/sdk";

const client = new TypeSafeClient({
  apiKey: process.env.LANGSMITH_API_KEY,
  baseURL: "https://gateway.smith.langchain.com",
});

const response = await client.systemOne({
  state: "Hello!",
  model: "semif-qwen3.5-4b",
  questions: {
    is_helpful: noul("Does this explain what an LLM gateway does?"),
  },
});
```

#### cURL
```bash
curl https://gateway.smith.langchain.com/v1/systemone \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "state": "Hello!",
      "model": "semif-qwen3.5-4b",
      "questions": {
        "is_helpful": {
          "type": "noul",
          "instructions": "Does this explain what an LLM gateway does?"
        }
      }
    }'
```

## Understand decision models

Pass the text to evaluate in `state` and between 1 and 32 named questions in `questions`. Decision models support three question types:

* **`noul`**: Returns the probability that the answer is true.
* **`choice`**: Classifies the state into one of the supplied options.
* **`score`**: Scores the state against a rubric.

The response contains `answers` keyed by question name rather than a chat message. Streaming is not supported.

## SemIf

You can select SemIf from the hosted models on the gateway home page to get a request example. For regional base URLs, see [Regional gateways](llm-gateway-direct-model-access.md#use-a-regional-gateway).

SemIf calls do not consume Gateway Credits. Gateway [access](llm-gateway-model-access-policies.md), [rate-limit](llm-gateway-rate-limit-policies.md), and [budget policies](llm-gateway-spend-policies.md) still apply.

## TypeSafe (Jev)

The gateway also supports TypeSafe decision models with bring-your-own-key (BYOK). Configure `TYPESAFE_API_KEY` as a workspace [provider secret](llm-gateway-admin-setup.md#1-add-provider-secrets). See [TypeSafe setup](../integrations/providers/typesafe.md#setup) to create a key and install the LangChain integration.

Set `LANGSMITH_API_KEY` to your workspace-scoped LangSmith API key. The `typesafe/` prefix routes the request through your workspace's TypeSafe provider secret, not the hosted SemIf model. Do not pass your TypeSafe API key as the SDK's `api_key` or `apiKey` when calling the gateway. Use the gateway base URL without `/v1` for the SDKs:

#### Python
Install the TypeSafe SDK:

```bash
pip install typesafe-sdk
```

```python
import os

from typesafe_sdk import Noul, TypeSafeClient

client = TypeSafeClient(
    api_key=os.environ["LANGSMITH_API_KEY"],
    base_url="https://gateway.smith.langchain.com",
)

response = client.system_one(
    state="Hello!",
    model="typesafe/jev-1.13.0",
    questions={
        "is_helpful": Noul(
            instructions="Does this explain what an LLM gateway does?"
        ),
    },
)
```

#### JavaScript
Install the TypeSafe SDK:

```bash
npm install @typesafe-ai/sdk
```

```javascript
import { noul, TypeSafeClient } from "@typesafe-ai/sdk";

const client = new TypeSafeClient({
  apiKey: process.env.LANGSMITH_API_KEY,
  baseURL: "https://gateway.smith.langchain.com",
});

const response = await client.systemOne({
  state: "Hello!",
  model: "typesafe/jev-1.13.0",
  questions: {
    is_helpful: noul("Does this explain what an LLM gateway does?"),
  },
});
```

#### cURL
```bash
curl https://gateway.smith.langchain.com/v1/systemone \
    -H "Authorization: Bearer $LANGSMITH_API_KEY" \
    -H "Content-Type: application/json" \
    -d '{
      "state": "Hello!",
      "model": "typesafe/jev-1.13.0",
      "questions": {
        "is_helpful": {
          "type": "noul",
          "instructions": "Does this explain what an LLM gateway does?"
        }
      }
    }'
```

## See also

* [Admin setup](llm-gateway-admin-setup.md): Grant gateway access without configuring a provider secret for SemIf.
* [TypeSafe integration](../integrations/providers/typesafe.md): Use TypeSafe decision models through LangChain.

***

> [!NOTE]
> [Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/llm-gateway-decision-models.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
