---
title: "Tavily map integration"
description: "Integrate with the Tavily map tool using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/tools/tavily_map"
category: "docs"
tags: [docs, integrations, tools, tavily_map]
---

# Tavily map integration

> Integrate with the Tavily map tool using LangChain Python.

[Tavily](https://tavily.com) is a search engine built specifically for AI agents (LLMs), delivering real-time, accurate, and factual results at speed. Tavily offers a [Map](https://docs.tavily.com/documentation/api-reference/endpoint/map) endpoint that traverses websites and returns a list of discovered URLs without extracting page content, which is ideal for understanding site structure or locating specific pages on a large site.

## Overview

### Integration details

| Class | Package | Serializable | [JS support](../../javascript/integrations/tools/tavily_map.md) | Version |
| :- | :- | :-: | :-: | :-: |
| [`TavilyMap`](https://reference.langchain.com/python/langchain-tavily/tavily_map/TavilyMap) | [`langchain-tavily`](https://reference.langchain.com/python/langchain-tavily/) | ✅ | ✅ | ![PyPI - Version](https://img.shields.io/pypi/v/langchain-tavily?style=flat-square\&label=%20) |

### Tool features

| [Returns artifact](../../langchain/tools.md) | Native async | Return data | Pricing |
| :-: | :-: | :-: | :-: |
| ❌ | ✅ | list of discovered URLs | 1,000 free credits / month |

## Setup

The integration lives in the `langchain-tavily` package.

```python
pip install -qU langchain-tavily
```

### Credentials

We also need to set our Tavily API key. You can get an API key by visiting [this site](https://app.tavily.com/sign-in) and creating an account.

```python
import getpass
import os

if not os.environ.get("TAVILY_API_KEY"):
    os.environ["TAVILY_API_KEY"] = getpass.getpass("Tavily API key:\n")
```

## Instantiation

The tool accepts the following parameters during instantiation:

* `max_depth` (optional, int): Maximum number of hops from the starting URL. Default is 1.
* `max_breadth` (optional, int): Maximum number of URLs returned per level. Default is 20.
* `limit` (optional, int): Maximum total number of URLs to return. Default is 50.
* `instructions` (optional, str): Natural-language instructions that guide the map traversal.
* `select_paths` (optional, list\[str]): Only include URLs containing these path regexes.
* `select_domains` (optional, list\[str]): Only include URLs from these domain regexes.
* `exclude_paths` (optional, list\[str]): Skip URLs containing these path regexes.
* `exclude_domains` (optional, list\[str]): Skip URLs from these domain regexes.
* `allow_external` (optional, bool): Allow the map to follow external links.

For a comprehensive overview of the available parameters, refer to the [Tavily Map API documentation](https://docs.tavily.com/documentation/api-reference/endpoint/map).

```python
from langchain_tavily import TavilyMap

tool = TavilyMap(
    max_depth=1,
    max_breadth=20,
    limit=50,
    # allow_external=False,
)
```

## Invocation

### [Invoke directly with args](../../langchain/tools.md)

The Tavily map tool accepts the following arguments during invocation:

* `url` (required): The base URL to start mapping from.
* The following arguments can also be set during invocation: `instructions`, `select_paths`, `select_domains`, `exclude_paths`, `exclude_domains`, `allow_external`.

NOTE: The optional arguments are available for agents to dynamically set. If you set an argument during instantiation and then invoke the tool with a different value, the tool will use the value you passed during invocation.

```python
tool.invoke({"url": "https://docs.tavily.com"})
```

```json
{
  "base_url": "https://docs.tavily.com",
  "results": [
    "https://docs.tavily.com/",
    "https://docs.tavily.com/changelog",
    "https://docs.tavily.com/welcome",
    "https://docs.tavily.com/documentation/mcp",
    "https://docs.tavily.com/documentation/about",
  ],
  "response_time": 0.37
}
```

### [Invoke with ToolCall](../../langchain/tools.md)

We can also invoke the tool with a model-generated ToolCall, in which case a ToolMessage will be returned:

```python
model_generated_tool_call = {
    "args": {"url": "https://docs.tavily.com", "instructions": "Find API reference pages"},
    "id": "1",
    "name": "tavily_map",
    "type": "tool_call",
}
tool_msg = tool.invoke(model_generated_tool_call)

print(tool_msg.content[:400])
```

## Use within an agent

We can use the map tool directly with an agent by binding it to the model. The agent can then dynamically set instructions and filters to discover the URLs it needs.

> [tab] OpenAI
>
> 👉 Read the [OpenAI chat model integration docs](../chat/openai.md)
>
**pip**

```bash
> pip install -U "langchain[openai]"
```
>
**uv**

```bash
> uv add "langchain[openai]"
```
>
**init_chat_model**

```python
> import os
> from langchain.chat_models import init_chat_model
>
> os.environ["OPENAI_API_KEY"] = "sk-..."
>
> model = init_chat_model("gpt-5.5")
```
>
**Model Class**

```python
> import os
> from langchain_openai import ChatOpenAI
>
> os.environ["OPENAI_API_KEY"] = "sk-..."
>
> model = ChatOpenAI(model="gpt-5.5")
```

> [tab] Anthropic
>
> 👉 Read the [Anthropic chat model integration docs](../chat/anthropic.md)
>
**pip**

```bash
> pip install -U "langchain[anthropic]"
```
>
**uv**

```bash
> uv add "langchain[anthropic]"
```
>
**init_chat_model**

```python
> import os
> from langchain.chat_models import init_chat_model
>
> os.environ["ANTHROPIC_API_KEY"] = "sk-..."
>
> model = init_chat_model("claude-sonnet-4-6")
```
>
**Model Class**

```python
> import os
> from langchain_anthropic import ChatAnthropic
>
> os.environ["ANTHROPIC_API_KEY"] = "sk-..."
>
> model = ChatAnthropic(model="claude-sonnet-4-6")
```

> [tab] Azure
>
> 👉 Read the [Azure chat model integration docs](../chat/azure_chat_openai.md)
>
**pip**

```bash
> pip install -U "langchain[openai]"
```
>
**uv**

```bash
> uv add "langchain[openai]"
```
>
**init_chat_model**

```python
> import os
> from langchain.chat_models import init_chat_model
>
> os.environ["AZURE_OPENAI_API_KEY"] = "..."
> os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
> os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"
>
> model = init_chat_model(
>     "azure_openai:gpt-5.5",
>     azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
> )
```
>
**Model Class**

```python
> import os
> from langchain_openai import AzureChatOpenAI
>
> os.environ["AZURE_OPENAI_API_KEY"] = "..."
> os.environ["AZURE_OPENAI_ENDPOINT"] = "..."
> os.environ["OPENAI_API_VERSION"] = "2025-03-01-preview"
>
> model = AzureChatOpenAI(
>     model="gpt-5.5",
>     azure_deployment=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"]
> )
```

> [tab] Google Gemini
>
> 👉 Read the [Google GenAI chat model integration docs](../chat/google_generative_ai.md)
>
**pip**

```bash
> pip install -U "langchain[google-genai]"
```
>
**uv**

```bash
> uv add "langchain[google-genai]"
```
>
**init_chat_model**

```python
> import os
> from langchain.chat_models import init_chat_model
>
> os.environ["GOOGLE_API_KEY"] = "..."
>
> model = init_chat_model("google_genai:gemini-3.7-flash")
```
>
**Model Class**

```python
> import os
> from langchain_google_genai import ChatGoogleGenerativeAI
>
> os.environ["GOOGLE_API_KEY"] = "..."
>
> model = ChatGoogleGenerativeAI(model="gemini-3.7-flash")
```

> [tab] AWS Bedrock
>
> 👉 Read the [AWS Bedrock chat model integration docs](../chat/bedrock.md)
>
**pip**

```bash
> pip install -U "langchain[aws]"
```
>
**uv**

```bash
> uv add "langchain[aws]"
```
>
**init_chat_model**

```python
> from langchain.chat_models import init_chat_model
>
> # Follow the steps here to configure your credentials:
> # https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html
>
> model = init_chat_model(
>     "us.anthropic.claude-sonnet-4-6",
>     model_provider="bedrock_converse",
> )
```
>
**Model Class**

```python
> from langchain_aws import ChatBedrock
>
> model = ChatBedrock(model="us.anthropic.claude-sonnet-4-6")
```

> [tab] HuggingFace
>
> 👉 Read the [HuggingFace chat model integration docs](../chat/huggingface.md)
>
**pip**

```bash
> pip install -U "langchain[huggingface]"
```
>
**uv**

```bash
> uv add "langchain[huggingface]"
```
>
**init_chat_model**

```python
> import os
> from langchain.chat_models import init_chat_model
>
> os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."
>
> model = init_chat_model(
>     "microsoft/Phi-3-mini-4k-instruct",
>     model_provider="huggingface",
>     temperature=0.7,
>     max_tokens=1024,
> )
```
>
**Model Class**

```python
> import os
> from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
>
> os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."
>
> llm = HuggingFaceEndpoint(
>     repo_id="microsoft/Phi-3-mini-4k-instruct",
>     temperature=0.7,
>     max_length=1024,
> )
> model = ChatHuggingFace(llm=llm)
```

> [tab] OpenRouter
>
> 👉 Read the [OpenRouter chat model integration docs](../chat/openrouter.md)
>
**pip**

```bash
> pip install -U "langchain-openrouter"
```
>
**uv**

```bash
> uv add "langchain-openrouter"
```
>
**init_chat_model**

```python
> import os
> from langchain.chat_models import init_chat_model
>
> os.environ["OPENROUTER_API_KEY"] = "sk-..."
>
> model = init_chat_model(
>     "auto",
>     model_provider="openrouter",
> )
```
>
**Model Class**

```python
> import os
> from langchain_openrouter import ChatOpenRouter
>
> os.environ["OPENROUTER_API_KEY"] = "sk-..."
>
> model = ChatOpenRouter(model="auto")
```

```python
if not os.environ.get("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = getpass.getpass("OPENAI_API_KEY:\n")
```

```python
from langchain.chat_models import init_chat_model

model = init_chat_model(model="gpt-5.5", model_provider="openai", temperature=0)
```

```python
from langchain_tavily import TavilyMap
from langchain.agents import create_agent

tavily_map_tool = TavilyMap(max_depth=2, max_breadth=20, limit=30)

agent = create_agent(model, [tavily_map_tool])

user_input = "Map https://docs.tavily.com and list URLs that look like API reference pages."

stream = agent.stream_events({"messages": user_input}, version="v3")
for snapshot in stream.values:
    snapshot["messages"][-1].pretty_print()
```

***

## API reference

For detailed documentation of all Tavily Map API features and configurations head to the API reference: [docs.tavily.com/documentation/api-reference/endpoint/map](https://docs.tavily.com/documentation/api-reference/endpoint/map)

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/tavily_map.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
