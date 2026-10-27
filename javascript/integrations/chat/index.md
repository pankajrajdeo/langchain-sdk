---
title: "Chat model integrations"
description: "Integrate with chat models using LangChain JavaScript."
source: "https://docs.langchain.com/oss/javascript/integrations/chat/index"
category: "docs"
tags: [docs, javascript, integrations, chat]
---

# Chat model integrations

> Integrate with chat models using LangChain JavaScript.

[Chat models](../../langchain/models.md) are language models that use a sequence of [messages](../../langchain/messages.md) as inputs and return messages as outputs (as opposed to plaintext) (Older models that do not follow the chat model interface and instead use an interface that takes a string as input and returns a string as output. These models typically do not include the prefix 'Chat' in their name or include 'LLM' as a suffix.).

## Install and use

> [!TIP]
>
> See [this section for general instructions on installing LangChain packages](../../langchain/install.md).

> **OpenAI**
>
> Install:
>
**npm**

```bash
> npm install @langchain/openai @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/openai @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/openai @langchain/core
```
>
> Add environment variables:
>
```bash
> OPENAI_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { ChatOpenAI } from "@langchain/openai";
>
> const model = new ChatOpenAI({ model: "gpt-5.4-mini" });
```
>
```javascript
> await model.invoke("Hello, world!")
```

> **Anthropic**
>
> Install:
>
**npm**

```bash
> npm i @langchain/anthropic @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/anthropic @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/anthropic @langchain/core
```
>
> Add environment variables:
>
```bash
> ANTHROPIC_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { ChatAnthropic } from "@langchain/anthropic";
>
> const model = new ChatAnthropic({
> model: "claude-sonnet-4-6",
> temperature: 0
> });
```
>
```javascript
> await model.invoke("Hello, world!")
```

> **Google Gemini**
>
> Install:
>
**npm**

```bash
> npm install @langchain/google @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/google @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/google @langchain/core
```
>
> Add environment variables:
>
```bash
> GOOGLE_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { ChatGoogle } from "@langchain/google";
>
> const model = new ChatGoogle("gemini-2.5-flash");
```
>
```javascript
> await model.invoke("Hello, world!")
```

> **MistralAI**
>
> Install:
>
**npm**

```bash
> npm install @langchain/mistralai @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/mistralai @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/mistralai @langchain/core
```
>
> Add environment variables:
>
```bash
> MISTRAL_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { ChatMistralAI } from "@langchain/mistralai";
>
> const model = new ChatMistralAI({
> model: "mistral-large-latest",
> temperature: 0
> });
```
>
```javascript
> await model.invoke("Hello, world!")
```

> **Groq**
>
> Install:
>
**npm**

```bash
> npm install @langchain/groq @langchain/core
```
>
**yarn**

```bash
> yarn add @langchain/groq @langchain/core
```
>
**pnpm**

```bash
> pnpm add @langchain/groq @langchain/core
```
>
> Add environment variables:
>
```bash
> GROQ_API_KEY=your-api-key
```
>
> Instantiate the model:
>
```typescript
> import { ChatGroq } from "@langchain/groq";
>
> const model = new ChatGroq({
> model: "openai/gpt-oss-120b",
> temperature: 0
> });
```
>
```javascript
> await model.invoke("Hello, world!")
```

## Featured models

> [!NOTE]
>
> **While these LangChain classes support the indicated advanced feature**, you may need to refer to provider-specific documentation to learn which hosted models or backends support the feature.

| Model | Stream | [Tool Calling](../../langchain/tools.md) | [`withStructuredOutput()`](../../langchain/models.md#structured-output) | [`Multimodal`](../../langchain/messages.md#multimodal) | Downloads |
| :- | :- | :- | :- | :- | :- |
| [`ChatOpenAI`](openai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/openai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/openai) |
| [`ChatAnthropic`](anthropic.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/anthropic?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/anthropic) |
| [`ChatBedrockConverse`](bedrock_converse.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/aws?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/aws) |
| [`ChatGroq`](groq.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/groq?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/groq) |
| [`ChatOllama`](ollama.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/ollama?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/ollama) |
| [`ChatMistralAI`](mistral.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/mistralai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/mistralai) |
| [`ChatGoogle`](google.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/google?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/google) |
| [`ChatXAI`](xai.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/xai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/xai) |
| [`ChatCohere`](cohere.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/cohere?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/cohere) |
| [`ChatFireworks`](fireworks.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/fireworks?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/fireworks) |
| [`ChatCloudflareWorkersAI`](cloudflare_workersai.md) | ✅ | ❌ | ❌ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/cloudflare?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/cloudflare) |
| [`ChatTogetherAI`](togetherai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/together-ai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/together-ai) |
| [`ChatPerplexity`](perplexity.md) | ✅ | ❌ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/perplexity?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/perplexity) |

See the [full list of chat model integrations](#all-chat-models) below for more options.

## Routers & proxies

Routers and proxies give you access to models from multiple providers through a single API and credential. They can simplify billing, let you switch between models without changing integrations, and offer features like automatic fallbacks.

| Provider | Integration | Description |
| - | - | - |
| [OpenRouter](https://openrouter.ai/) | [`ChatOpenRouter`](openrouter.md) | Unified access to models from OpenAI, Anthropic, Google, Meta, and more |
| [FuturMix](https://futurmix.ai/) | [`ChatOpenAI`](https://futurmix.ai/) | Unified AI gateway for 22+ models with OpenAI-compatible API and 99.99% SLA |

## Chat Completions API

Certain model providers offer endpoints that are compatible with OpenAI's (legacy) [Chat Completions API](https://platform.openai.com/docs/guides/completions). In such case, you can use [`ChatOpenAI`](openai.md) with a custom `base_url` to connect to these endpoints. Note that features built on top of the Chat Completions API may not be fully supported by `ChatOpenAI`; in such cases, consider using a provider-specific class if available.

## All chat models

| Model | Stream | [Tool Calling](../../langchain/tools.md) | [`withStructuredOutput()`](../../langchain/models.md#structured-output) | [`Multimodal`](../../langchain/messages.md#multimodal) | Downloads |
| :- | :- | :- | :- | :- | :- |
| [`AzureChatOpenAI`](azure.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/openai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/openai) |
| [`ChatOpenAI`](openai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/openai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/openai) |
| [`ChatAnthropic`](anthropic.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/anthropic?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/anthropic) |
| [`ChatGoogleGenerativeAI`](google_generative_ai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/google-genai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/google-genai) |
| [`ChatBedrockConverse`](bedrock_converse.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/aws?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/aws) |
| [`ChatVertexAI`](google_vertex_ai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/google-vertexai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/google-vertexai) |
| [`ChatGroq`](groq.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/groq?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/groq) |
| [`ChatOllama`](ollama.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/ollama?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/ollama) |
| [`ChatMistralAI`](mistral.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/mistralai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/mistralai) |
| [`ChatGoogle`](google.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/google?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/google) |
| [`ChatXAI`](xai.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/xai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/xai) |
| [`ChatCohere`](cohere.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/cohere?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/cohere) |
| [`ChatOpenRouter`](openrouter.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/openrouter?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/openrouter) |
| [`ChatDeepSeek`](deepseek.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/deepseek?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/deepseek) |
| [`ChatCerebras`](cerebras.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/cerebras?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/cerebras) |
| [`ChatFireworks`](fireworks.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/fireworks?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/fireworks) |
| [`ChatBaiduQianfan`](baidu_qianfan.md) | | | | | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/baidu-qianfan?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/baidu-qianfan) |
| [`ChatCloudflareWorkersAI`](cloudflare_workersai.md) | ✅ | ❌ | ❌ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/cloudflare?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/cloudflare) |
| [`ChatTogetherAI`](togetherai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/together-ai?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/together-ai) |
| [`ChatWatsonx`](ibm.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/ibm?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/ibm) |
| [`ChatPerplexity`](perplexity.md) | ✅ | ❌ | ✅ | ❌ | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/perplexity?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/perplexity) |
| [`ChatYandexGPT`](yandex.md) | | | | | [  ![Downloads per month](https://img.shields.io/npm/dm/@langchain/yandex?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@langchain/yandex) |
| [`ChatInterfaze`](https://interfaze.ai/docs) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@interfaze-ai/langchain?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@interfaze-ai/langchain) |
| [`ChatKServe`](https://gitlab.com/bitkaio/langchain/kserve-provider) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@bitkaio/langchain-kserve?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@bitkaio/langchain-kserve) |
| [`ChatWebLLM`](https://github.com/ykoh42/web-llm-adapters/blob/main/packages/langchain-web-llm/README.md) | ✅ | ✅ | ✅ | | [  ![Downloads per month](https://img.shields.io/npm/dm/langchain-web-llm?style=flat-square\&label=%20&)](https://www.npmjs.com/package/langchain-web-llm) |
| [`RecallToolkit`](https://recallmem.dev/guides/langchain) | | | | | [  ![Downloads per month](https://img.shields.io/npm/dm/@recall-memory/langchain?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@recall-memory/langchain) |
| [`ChatSCX`](https://scx.ai/) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://img.shields.io/npm/dm/@scx-ai/langchain?style=flat-square\&label=%20&)](https://www.npmjs.com/package/@scx-ai/langchain) |
| [`Auxen`](https://auxen.ai) | ✅ | ✅ | ✅ | ❌ | N/A |
| [`ChatEmpirioLabs`](https://docs.empiriolabs.ai/integrations#langchain) | ✅ | ✅ | ✅ | ✅ | N/A |
| [`FakeListChatModel`](fake.md) | | | | | N/A |
| [`FuturMix`](https://futurmix.ai/) | ✅ | ✅ | ✅ | ✅ | N/A |
| [`Tuning Engines`](https://www.tuningengines.com/) | ✅ | ✅ | ✅ | ❌ | N/A |

> [!NOTE]
>
> If you'd like to contribute an integration, see [Contributing integrations](../../contributing.md#add-a-new-integration).

***

[Connect these docs](../../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/javascript/integrations/chat/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
