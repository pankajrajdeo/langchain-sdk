---
title: "Gmail toolkit integration"
description: "Integrate with the Gmail toolkit using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/tools/google_gmail"
category: "docs"
tags: [docs, integrations, tools, google_gmail]
---

# Gmail toolkit integration

> Integrate with the Gmail toolkit using LangChain Python.

This will help you get started with the Gmail [toolkit](google_gmail.md). This toolkit interacts with the Gmail API to read messages, draft and send messages, and more. For detailed documentation of all `GmailToolkit` features and configurations head to the [API reference](https://reference.langchain.com/python/langchain-google-community/gmail/toolkit/GmailToolkit).

## Setup

To use this toolkit, you will need to set up your credentials explained in the [Gmail API docs](https://developers.google.com/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application). Once you've downloaded the `credentials.json` file, you can start using the Gmail API.

### Installation

This toolkit lives in the `langchain-google-community` package. We'll need the `gmail` extra:

```python
pip install -qU langchain-google-community\[gmail\]
```

To enable automated tracing of individual tools, set your [LangSmith](../../langsmith/observability.md) API key:

```python
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
```

## Instantiation

By default the toolkit reads the local `credentials.json` file. You can also manually provide a `Credentials` object.

```python
from langchain_google_community import GmailToolkit

toolkit = GmailToolkit()
```

### Customizing authentication

Behind the scenes, a `googleapi` resource is created using the following methods.
you can manually build a `googleapi` resource for more auth control.

```python
from langchain_google_community.gmail.utils import (
    build_resource_service,
    get_google_credentials,
)

# Can review scopes here https://developers.google.com/gmail/api/auth/scopes
# For instance, readonly scope is 'https://www.googleapis.com/auth/gmail.readonly'
credentials = get_google_credentials(
    token_file="token.json",
    scopes=["https://mail.google.com/"],
    client_secrets_file="credentials.json",
)
api_resource = build_resource_service(credentials=credentials)
toolkit = GmailToolkit(api_resource=api_resource)
```

## Tools

View available tools:

```python
tools = toolkit.get_tools()
tools
```

```text
[GmailCreateDraft(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>),
 GmailSendMessage(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>),
 GmailSearch(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>),
 GmailGetMessage(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>),
 GmailGetThread(api_resource=<googleapiclient.discovery.Resource object at 0x1094509d0>)]
```

* [GmailCreateDraft](https://reference.langchain.com/python/langchain-google-community/gmail/create_draft/GmailCreateDraft)
* [GmailSendMessage](https://reference.langchain.com/python/langchain-google-community/gmail/send_message/GmailSendMessage)
* [GmailSearch](https://reference.langchain.com/python/langchain-google-community/gmail/search/GmailSearch)
* [GmailGetMessage](https://reference.langchain.com/python/langchain-google-community/gmail/get_message/GmailGetMessage)
* [GmailGetThread](https://reference.langchain.com/python/langchain-google-community/gmail/get_thread/GmailGetThread)

## Use within an agent

Below we show how to incorporate the toolkit into an [agent](../../langchain/agents.md).

We will need an LLM or chat model:

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
> model = init_chat_model("gpt-6.1-sol")
```
>
**Model Class**

```python
> import os
> from langchain_openai import ChatOpenAI
>
> os.environ["OPENAI_API_KEY"] = "sk-..."
>
> model = ChatOpenAI(model="gpt-6.1-sol")
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
>     "azure_openai:gpt-6.1-sol",
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
>     model="gpt-6.1-sol",
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
# | output: false
# | echo: false

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-5.4-mini", temperature=0)
```

```python
from langchain.agents import create_agent

agent_executor = create_agent(llm, tools)
```

```python
example_query = "Draft an email to fake@fake.com thanking them for coffee."

stream = agent_executor.stream_events(
    {"messages": [("user", example_query)]},
    version="v3",
)
for snapshot in stream.values:
    snapshot["messages"][-1].pretty_print()
```

```text
================================ Human Message =================================

Draft an email to fake@fake.com thanking them for coffee.
================================== Ai Message ==================================
Tool Calls:
  create_gmail_draft (call_slGkYKZKA6h3Mf1CraUBzs6M)
 Call ID: call_slGkYKZKA6h3Mf1CraUBzs6M
  Args:
    message: Dear Fake,

I wanted to take a moment to thank you for the coffee yesterday. It was a pleasure catching up with you. Let's do it again soon!

Best regards,
[Your Name]
    to: ['fake@fake.com']
    subject: Thank You for the Coffee
================================= Tool Message =================================
Name: create_gmail_draft

Draft created. Draft Id: r-7233782721440261513
================================== Ai Message ==================================

I have drafted an email to fake@fake.com thanking them for the coffee. You can review and send it from your email draft with the subject "Thank You for the Coffee".
```

***

## API reference

For detailed documentation of all `GmailToolkit` features and configurations head to the [API reference](https://reference.langchain.com/python/langchain-google-community/gmail/toolkit/GmailToolkit).

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/google_gmail.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
