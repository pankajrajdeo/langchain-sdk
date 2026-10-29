---
title: "Chat model integrations"
description: "Integrate with chat models using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/chat/index"
category: "docs"
tags: [docs, integrations, chat]
---

# Chat model integrations

> Integrate with chat models using LangChain Python.

[Chat models](../../langchain/models.md) are language models that use a sequence of [messages](../../langchain/messages.md) as inputs and return messages as outputs (as opposed to traditional, plaintext LLMs) (Older models that do not follow the chat model interface and instead use an interface that takes a string as input and returns a string as output. These models typically do not include the prefix 'Chat' in their name or include 'LLM' as a suffix.).

Integration components
Arrows show a typical retrieval flow. The highlighted component is the one this page covers.

### Typical retrieval flow

### Agent capabilities

### Execution and state

## Featured models

> [!NOTE]
>
> **While these LangChain classes support the indicated advanced feature**, you may need to refer to provider-specific documentation to learn which hosted models or backends support the feature.

| Model | Stream | [Tool calling](../../langchain/tools.md) | [Structured output](../../langchain/structured-output.md) | [Multimodal](../../langchain/messages.md#multimodal) | Downloads |
| :- | :- | :- | :- | :- | :- |
| [`AzureChatOpenAI`](azure_chat_openai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-openai/month)](https://pypi.org/project/langchain-openai/) |
| [`ChatOpenAI`](openai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-openai/month)](https://pypi.org/project/langchain-openai/) |
| [`ChatVertexAI`](google_vertex_ai.md) (deprecated) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-google-vertexai/month)](https://pypi.org/project/langchain-google-vertexai/) |
| [`ChatAnthropic`](anthropic.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-anthropic/month)](https://pypi.org/project/langchain-anthropic/) |
| [`ChatGoogleGenerativeAI`](google_generative_ai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-google-genai/month)](https://pypi.org/project/langchain-google-genai/) |
| [`ChatOllama`](ollama.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-ollama/month)](https://pypi.org/project/langchain-ollama/) |
| [`ChatGroq`](groq.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-groq/month)](https://pypi.org/project/langchain-groq/) |
| [`ChatLiteLLM`](litellm.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-litellm/month)](https://pypi.org/project/langchain-litellm/) |
| [`ChatMistralAI`](mistralai.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-mistralai/month)](https://pypi.org/project/langchain-mistralai/) |
| [`ChatHuggingFace`](huggingface.md) | ❌ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-huggingface/month)](https://pypi.org/project/langchain-huggingface/) |
| [`ChatOpenRouter`](openrouter.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-openrouter/month)](https://pypi.org/project/langchain-openrouter/) |
| [`ChatXAI`](xai.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-xai/month)](https://pypi.org/project/langchain-xai/) |
| [`ChatDeepSeek`](deepseek.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-deepseek/month)](https://pypi.org/project/langchain-deepseek/) |
| [`ChatCohere`](cohere.md) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-cohere/month)](https://pypi.org/project/langchain-cohere/) |
| [`ChatNVIDIA`](nvidia_ai_endpoints.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-nvidia-ai-endpoints/month)](https://pypi.org/project/langchain-nvidia-ai-endpoints/) |
| [`ChatDatabricks`](databricks.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/databricks-langchain/month)](https://pypi.org/project/databricks-langchain/) |
| [`ChatTogether`](together.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-together/month)](https://pypi.org/project/langchain-together/) |
| [`ChatAmazonNova`](amazon_nova.md) | ✅ | ✅ | ✅ | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-amazon-nova/month)](https://pypi.org/project/langchain-amazon-nova/) |

See the [full list of chat model integrations](#all-chat-models) below for more options.

## Routers & proxies

Routers and proxies give you access to models from multiple providers through a single API and credential. They can simplify billing, let you switch between models without changing integrations, and offer features like automatic fallbacks.

| Provider | Integration | Description |
| - | - | - |
| [OpenRouter](https://openrouter.ai/) | [`ChatOpenRouter`](openrouter.md) | Unified access to models from OpenAI, Anthropic, Google, Meta, and more |
| [LiteLLM](https://www.litellm.ai/) | [`ChatLiteLLMRouter`](litellm.md) | Unified interface for OpenAI, Anthropic, Azure, Hugging Face, and more with routing and fallbacks |

## Chat Completions API

Certain model providers offer endpoints that are compatible with OpenAI's [Chat Completions API](https://platform.openai.com/docs/api-reference/chat). In such cases, you can use [`ChatOpenAI`](openai.md) with a custom `base_url` to connect to these endpoints for basic chat functionality.

> [!WARNING]
>
> `ChatOpenAI` targets [official OpenAI API specifications](https://github.com/openai/openai-openapi) only. Non-standard response fields from third-party providers (e.g., `reasoning_content`, `reasoning`, `reasoning_details`) **are not extracted or preserved**. Use a provider-specific package when you need access to non-standard features.
>
> For instance, OpenRouter has a dedicated LangChain integration. See the [`ChatOpenRouter` guide](openrouter.md) for setup and usage.

## All chat models

| Model | Stream | [Tool calling](../../langchain/tools.md) | [Structured output](../../langchain/structured-output.md) | [Multimodal](../../langchain/messages.md#multimodal) | Downloads |
| :- | :- | :- | :- | :- | :- |
| [`AzureChatOpenAI`](azure_chat_openai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-openai/month)](https://pypi.org/project/langchain-openai/) |
| [`ChatOpenAI`](openai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-openai/month)](https://pypi.org/project/langchain-openai/) |
| [`vLLM`](vllm.md) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-openai/month)](https://pypi.org/project/langchain-openai/) |
| [`ChatAnthropicVertex`](google_anthropic_vertex.md) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-google-vertexai/month)](https://pypi.org/project/langchain-google-vertexai/) |
| [`ChatVertexAI`](google_vertex_ai.md) (deprecated) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-google-vertexai/month)](https://pypi.org/project/langchain-google-vertexai/) |
| [`ChatAnthropic`](anthropic.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-anthropic/month)](https://pypi.org/project/langchain-anthropic/) |
| [`ChatAnthropicTools`](anthropic_functions.md) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-anthropic/month)](https://pypi.org/project/langchain-anthropic/) |
| [`ChatGoogleGenerativeAI`](google_generative_ai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-google-genai/month)](https://pypi.org/project/langchain-google-genai/) |
| [`ChatBedrock`](bedrock.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-aws/month)](https://pypi.org/project/langchain-aws/) |
| [`ChatOllama`](ollama.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-ollama/month)](https://pypi.org/project/langchain-ollama/) |
| [`ChatGroq`](groq.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-groq/month)](https://pypi.org/project/langchain-groq/) |
| [`ChatLiteLLM`](litellm.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-litellm/month)](https://pypi.org/project/langchain-litellm/) |
| [`ChatMistralAI`](mistralai.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-mistralai/month)](https://pypi.org/project/langchain-mistralai/) |
| [`ChatHuggingFace`](huggingface.md) | ❌ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-huggingface/month)](https://pypi.org/project/langchain-huggingface/) |
| [`ChatOpenRouter`](openrouter.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-openrouter/month)](https://pypi.org/project/langchain-openrouter/) |
| [`ChatXAI`](xai.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-xai/month)](https://pypi.org/project/langchain-xai/) |
| [`ChatDeepSeek`](deepseek.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-deepseek/month)](https://pypi.org/project/langchain-deepseek/) |
| [`ChatCohere`](cohere.md) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-cohere/month)](https://pypi.org/project/langchain-cohere/) |
| [`ChatFireworks`](fireworks.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-fireworks/month)](https://pypi.org/project/langchain-fireworks/) |
| [`ChatNVIDIA`](nvidia_ai_endpoints.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-nvidia-ai-endpoints/month)](https://pypi.org/project/langchain-nvidia-ai-endpoints/) |
| [`AzureAIChatCompletionsModel`](azure_ai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-azure-ai/month)](https://pypi.org/project/langchain-azure-ai/) |
| [`ChatDatabricks`](databricks.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/databricks-langchain/month)](https://pypi.org/project/databricks-langchain/) |
| [`ChatWatsonx`](ibm_watsonx.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-ibm/month)](https://pypi.org/project/langchain-ibm/) |
| [`ChatPerplexity`](perplexity.md) | ✅ | ❌ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-perplexity/month)](https://pypi.org/project/langchain-perplexity/) |
| [`ChatCerebras`](cerebras.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-cerebras/month)](https://pypi.org/project/langchain-cerebras/) |
| [`ChatBaseten`](baseten.md) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-baseten/month)](https://pypi.org/project/langchain-baseten/) |
| [`ChatTogether`](together.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-together/month)](https://pypi.org/project/langchain-together/) |
| [`ChatOCIGenerativeAI`](oci_generative_ai.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-oci/month)](https://pypi.org/project/langchain-oci/) |
| [`ChatOCIModelDeployment`](oci_data_science.md) | ✅ | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-oci/month)](https://pypi.org/project/langchain-oci/) |
| [`ChatParallel`](parallel.md) | ✅ | ❌ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-parallel/month)](https://pypi.org/project/langchain-parallel/) |
| [`ChatQwen`](qwen.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-qwq/month)](https://pypi.org/project/langchain-qwq/) |
| [`ChatQwQ`](qwq.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-qwq/month)](https://pypi.org/project/langchain-qwq/) |
| [`ChatUpstage`](upstage.md) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-upstage/month)](https://pypi.org/project/langchain-upstage/) |
| [`ChatSambaNova`](sambanova.md) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-sambanova/month)](https://pypi.org/project/langchain-sambanova/) |
| [`ChatMoonshot`](https://github.com/ArcadiaLin/langchain-moonshot) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-moonshot/month)](https://pypi.org/project/langchain-moonshot/) |
| [`ChatCloudflareWorkersAI`](https://github.com/cloudflare/langchain-cloudflare) | ❌ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-cloudflare/month)](https://pypi.org/project/langchain-cloudflare/) |
| [`ChatClovaX`](https://guide.ncloud-docs.com/docs/clovastudio-dev-langchain) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-naver/month)](https://pypi.org/project/langchain-naver/) |
| [`Inferrail`](https://github.com/domondi1/inferrail/blob/main/docs/recipes/agent-run-budget.md?ref=langchain-docs#langchain) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/inferrail/month)](https://pypi.org/project/inferrail/) |
| [`ChatNebius`](https://github.com/nebius/langchain-nebius) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-nebius/month)](https://pypi.org/project/langchain-nebius/) |
| [`ChatGradient`](https://docs.digitalocean.com/products/ai-platform/) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-gradient/month)](https://pypi.org/project/langchain-gradient/) |
| [`ChatAmazonNova`](amazon_nova.md) | ✅ | ✅ | ✅ | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-amazon-nova/month)](https://pypi.org/project/langchain-amazon-nova/) |
| [`ChatEmpirioLabs`](https://docs.empiriolabs.ai) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-empiriolabs/month)](https://pypi.org/project/langchain-empiriolabs/) |
| [`ChatWriter`](https://dev.writer.com/home/introduction) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-writer/month)](https://pypi.org/project/langchain-writer/) |
| [`ChatTopxAI`](https://ai.topxea.com/docs/use-topxai-with-langchain) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-topxai/month)](https://pypi.org/project/langchain-topxai/) |
| [`ChatAI21`](https://docs.ai21.com/home) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-ai21/month)](https://pypi.org/project/langchain-ai21/) |
| [`ChatAceDataCloud`](https://github.com/AceDataCloud/LangChain) | ✅ | ✅ | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-acedatacloud/month)](https://pypi.org/project/langchain-acedatacloud/) |
| [`ChatCrusoe`](crusoe.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-crusoe/month)](https://pypi.org/project/langchain-crusoe/) |
| [`ChatFlexAI`](https://docs.flex.ai/inference-api/agents/langchain) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-flexai/month)](https://pypi.org/project/langchain-flexai/) |
| [`ChatRouter`](https://github.com/danielpolok/langchain-model-router) | ✅ | ✅ | ✅ | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-model-router/month)](https://pypi.org/project/langchain-model-router/) |
| [`ChatPredictionGuard`](https://github.com/predictionguard/langchain-predictionguard) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-predictionguard/month)](https://pypi.org/project/langchain-predictionguard/) |
| [`ChatDiffbot`](https://github.com/diffbot/langchain-diffbot) | ✅ | ❌ | ❌ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-diffbot/month)](https://pypi.org/project/langchain-diffbot/) |
| [`ChatAimlapi`](https://docs.aimlapi.com/) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-aimlapi/month)](https://pypi.org/project/langchain-aimlapi/) |
| [`RecallMiddleware`](https://recallmem.dev/guides/langchain) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-recall/month)](https://pypi.org/project/langchain-recall/) |
| [`ChatContextual`](https://docs.contextual.ai/) | ❌ | ❌ | ❌ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-contextual/month)](https://pypi.org/project/langchain-contextual/) |
| [`ChatHeabsy`](https://heabsy.com/integrations/langchain) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-heabsy/month)](https://pypi.org/project/langchain-heabsy/) |
| [`ChatDoubleword`](https://docs.doubleword.ai/inference-api/intro-to-doubleword-inference) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-doubleword/month)](https://pypi.org/project/langchain-doubleword/) |
| [`ChatAISL`](https://github.com/StudioPlatforms/aistupidlevel-sdk/blob/main/langchain-python/README.md) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-aistupidlevel/month)](https://pypi.org/project/langchain-aistupidlevel/) |
| [`ChatAbso`](https://github.com/lunary-ai/langchain-abso) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-abso/month)](https://pypi.org/project/langchain-abso/) |
| [`ChatBrainiall`](https://app.brainiall.com/docs) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-brainiall/month)](https://pypi.org/project/langchain-brainiall/) |
| [`ChatKServe`](https://gitlab.com/bitkaio/langchain/kserve-provider) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-kserve/month)](https://pypi.org/project/langchain-kserve/) |
| [`ChatHubris`](https://hubris.pw/docs/integrations/langchain) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-hubris/month)](https://pypi.org/project/langchain-hubris/) |
| [`ModelScopeChatEndpoint`](https://github.com/modelscope/langchain-modelscope) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-modelscope-integration/month)](https://pypi.org/project/langchain-modelscope-integration/) |
| [`ChatSarvam`](https://docs.sarvam.ai/api/integration/langchain) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-sarvamcloud/month)](https://pypi.org/project/langchain-sarvamcloud/) |
| [`ChatFeatherlessAI`](https://github.com/featherless-ai-integrations/langchain-featherless-ai) | ✅ | ❌ | ❌ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-featherless-ai/month)](https://pypi.org/project/langchain-featherless-ai/) |
| [`ChatKinetica`](https://github.com/kineticadb/langchain-kinetica) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-kinetica/month)](https://pypi.org/project/langchain-kinetica/) |
| [`ChatYutoriNavigator`](https://docs.yutori.com) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-yutori/month)](https://pypi.org/project/langchain-yutori/) |
| [`ChatXinference`](https://github.com/TheSongg/langchain-xinference) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-xinference/month)](https://pypi.org/project/langchain-xinference/) |
| [`ChatRunPod`](https://docs.runpod.io/overview) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-runpod/month)](https://pypi.org/project/langchain-runpod/) |
| [`SpendGuardChatModel`](https://agenticspendguard.dev) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/spendguard-sdk/month)](https://pypi.org/project/spendguard-sdk/) |
| [`ChatOpenZoo`](https://github.com/staccDOTsol/langchain-openzoo) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-openzoo/month)](https://pypi.org/project/langchain-openzoo/) |
| [`ChatAppleFoundationModels`](https://github.com/rajanshxrma/langchain-apple-foundation-models) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-apple-foundation-models/month)](https://pypi.org/project/langchain-apple-foundation-models/) |
| [`Apertis`](https://docs.apertis.ai/api/sdks/langchain/) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-apertis/month)](https://pypi.org/project/langchain-apertis/) |
| [`ChatAlephantAI`](https://alephant.io/) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-alephantai/month)](https://pypi.org/project/langchain-alephantai/) |
| [`ChatPipeshift`](https://github.com/pipeshift-org/langchain-pipeshift) | ✅ | ❌ | ❌ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-pipeshift/month)](https://pypi.org/project/langchain-pipeshift/) |
| [`ChatInterfaze`](https://interfaze.ai/docs) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/interfaze-langchain/month)](https://pypi.org/project/interfaze-langchain/) |
| [`ChatGreenNode`](https://github.com/greennode-ai/langchain-greennode) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-greennode/month)](https://pypi.org/project/langchain-greennode/) |
| [`ChatTelnyx`](https://developers.telnyx.com/docs/inference/models) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-telnyx/month)](https://pypi.org/project/langchain-telnyx/) |
| [`ChatNeuralwatt`](https://neuralwatt.com) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-neuralwatt/month)](https://pypi.org/project/langchain-neuralwatt/) |
| [`ChatThalam`](https://thalam.ai/docs) | ✅ | ✅ | ✅ | ✅ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-thalam/month)](https://pypi.org/project/langchain-thalam/) |
| [`ChatNetmind`](https://github.com/protagolabs/langchain-netmind) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-netmind/month)](https://pypi.org/project/langchain-netmind/) |
| [`ChatDuel`](https://duelagents.com) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-duel/month)](https://pypi.org/project/langchain-duel/) |
| [`ChatSeekrFlow`](https://github.com/benfaircloth/langchain-seekrflow) | ✅ | ✅ | ✅ | ❌ | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-seekrflow/month)](https://pypi.org/project/langchain-seekrflow/) |
| [`ChatKalibr`](https://kalibr.systems/docs) | | | | | [  ![Downloads per month](https://static.pepy.tech/badge/langchain-kalibr/month)](https://pypi.org/project/langchain-kalibr/) |
| [`1Claw`](https://docs.1claw.xyz) | ✅ | ✅ | ✅ | ❌ | N/A |
| [`API-Route`](https://www.api-route.com/docs/overview) | | | | | N/A |
| [`Auxen`](https://auxen.ai) | ✅ | ✅ | ✅ | ❌ | N/A |
| [`Cheaper Inference`](https://cheaperinference.com/docs) | ✅ | ✅ | ✅ | ✅ | N/A |
| [`DaoXE`](https://daoxe.com) | ✅ | ✅ | ✅ | ✅ | N/A |
| [`FuturMix`](https://futurmix.ai/) | ✅ | ✅ | ✅ | ✅ | N/A |
| [`GPTZZZ`](https://gptzzz.ai/docs/) | ✅ | ✅ | ✅ | ✅ | N/A |
| [`Snowflake Cortex REST API`](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-rest-api) | ✅ | ✅ | ✅ | ❌ | N/A |
| [`Synthorai`](https://synthorai.io/docs/) | | | | | N/A |
| [`TokenMix`](https://tokenmix.ai/docs) | ✅ | ✅ | ✅ | ❌ | N/A |
| [`Tuning Engines`](https://www.tuningengines.com/) | ✅ | ✅ | ✅ | ❌ | N/A |

> [!NOTE]
>
> If you'd like to contribute an integration, see [Contributing integrations](../../contributing.md#add-a-new-integration).

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/chat/index.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
