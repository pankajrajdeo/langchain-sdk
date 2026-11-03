---
title: "Google calendar toolkit integration"
description: "Integrate with the Google calendar toolkit using LangChain Python."
source: "https://docs.langchain.com/oss/python/integrations/tools/google_calendar"
category: "docs"
tags: [docs, integrations, tools, google_calendar]
---

# Google calendar toolkit integration

> Integrate with the Google calendar toolkit using LangChain Python.

> [Google Calendar](https://workspace.google.com/intl/en-419/products/calendar/) is a product of Google Workspace that allows users to organize their schedules and events. It is a cloud-based calendar that allows users to create, edit, and delete events. It also allows users to share their calendars with others.

## Overview

This notebook will help you get started with the Google Calendar Toolkit. This toolkit interacts with the Google Calendar API to perform various operations on the calendar. It allows you to:

* Create events.
* Search events.
* Update events.
* Move events between different calendars.
* Delete events.
* List events.

## Setup

To use this toolkit, you will need to:

1. Have a Google account with access to Google Calendar.
2. Set up your credentials as explained in the [Google Calendar API docs](https://developers.google.com/calendar/api/quickstart/python#authorize_credentials_for_a_desktop_application). Once you've downloaded the `credentials.json` file, you can start using the Google Calendar API.

To enable automated tracing of individual tools, set your [LangSmith](../../langsmith/observability.md) API key:

```python
os.environ["LANGSMITH_TRACING"] = "true"
os.environ["LANGSMITH_API_KEY"] = getpass.getpass("Enter your LangSmith API key: ")
```

### Installation

This toolkit lives in the `langchain-google-community` package of the [langchain-google](https://github.com/langchain-ai/langchain-google) repository. We'll need the `calendar` extra:

```python
pip install -qU langchain-google-community\[calendar\]
```

## Instantiation

By default the toolkit reads the local `credentials.json` file. You can also manually provide a `Credentials` object.

```python
from langchain_google_community import CalendarToolkit

toolkit = CalendarToolkit()
```

### Customizing authentication

Behind the scenes, a `googleapi` resource is created using the following methods. you can manually build a `googleapi` resource for more auth control.

```python
from langchain_google_community import CalendarToolkit
from langchain_google_community.calendar.utils import (
    build_resource_service,
    get_google_credentials,
)

# Can review scopes here: https://developers.google.com/calendar/api/auth
# For instance, readonly scope is https://www.googleapis.com/auth/calendar.readonly
credentials = get_google_credentials(
    token_file="token.json",
    scopes=["https://www.googleapis.com/auth/calendar"],
    client_secrets_file="credentials.json",
)

api_resource = build_resource_service(credentials=credentials)
toolkit = CalendarToolkit(api_resource=api_resource)
```

## Tools

View available tools:

```python
tools = toolkit.get_tools()
tools
```

```text
[CalendarCreateEvent(api_resource=<googleapiclient.discovery.Resource object at 0x10ad13fb0>),
 CalendarSearchEvents(api_resource=<googleapiclient.discovery.Resource object at 0x10ad13fb0>),
 CalendarUpdateEvent(api_resource=<googleapiclient.discovery.Resource object at 0x10ad13fb0>),
 GetCalendarsInfo(api_resource=<googleapiclient.discovery.Resource object at 0x10ad13fb0>),
 CalendarMoveEvent(api_resource=<googleapiclient.discovery.Resource object at 0x10ad13fb0>),
 CalendarDeleteEvent(api_resource=<googleapiclient.discovery.Resource object at 0x10ad13fb0>),
 GetCurrentDatetime(api_resource=<googleapiclient.discovery.Resource object at 0x10ad13fb0>)]
```

* [CalendarCreateEvent](https://reference.langchain.com/python/langchain-google-community/calendar/create_event/CalendarCreateEvent)
* [CalendarSearchEvents](https://reference.langchain.com/python/langchain-google-community/calendar/search_events/CalendarSearchEvents)
* [CalendarUpdateEvent](https://reference.langchain.com/python/langchain-google-community/calendar/update_event/CalendarUpdateEvent)
* [GetCalendarsInfo](https://reference.langchain.com/python/langchain-google-community/calendar/get_calendars_info/GetCalendarsInfo)
* [CalendarMoveEvent](https://reference.langchain.com/python/langchain-google-community/calendar/move_event/CalendarMoveEvent)
* [CalendarDeleteEvent](https://reference.langchain.com/python/langchain-google-community/calendar/delete_event/CalendarDeleteEvent)
* [GetCurrentDatetime](https://reference.langchain.com/python/langchain-google-community/calendar/current_datetime/GetCurrentDatetime)

## Invocation

### [Invoke directly with args](../../langchain/tools.md#create-tools)

You can invoke the tool directly by passing the required arguments in a dictionary format. Here is an example of creating a new event using the `CalendarCreateEvent` tool.

```python
from langchain_google_community.calendar.create_event import CalendarCreateEvent

tool = CalendarCreateEvent()
tool.invoke(
    {
        "summary": "Calculus exam",
        "start_datetime": "2025-07-11 11:00:00",
        "end_datetime": "2025-07-11 13:00:00",
        "timezone": "America/Mexico_City",
        "location": "UAM Cuajimalpa",
        "description": "Event created from the LangChain toolkit",
        "reminders": [{"method": "popup", "minutes": 60}],
        "conference_data": True,
        "color_id": "5",
    }
)
```

```text
'Event created: https://www.google.com/calendar/event?eid=amoxdjVsM2UzMW51Yjk2czc4ajhvaGdkcGcgam9yZ2VhbmczM0Bt'
```

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
example_query = "Create a green event for this afternoon to go for a 30-minute run."

stream = agent_executor.stream_events(
    {"messages": [("user", example_query)]},
    version="v3",
)
for snapshot in stream.values:
    snapshot["messages"][-1].pretty_print()
```

```text
================================ Human Message =================================

Create a green event for this afternoon to go for a 30-minute run.
================================== Ai Message ==================================
Tool Calls:
  get_current_datetime (call_drHRRhm6pdvcAuqagONUEKs5)
 Call ID: call_drHRRhm6pdvcAuqagONUEKs5
  Args:
================================= Tool Message =================================
Name: get_current_datetime

Time zone: America/Mexico_City, Date and time: 2025-04-02 19:07:30
================================== Ai Message ==================================
Tool Calls:
  create_calendar_event (call_p60zSVMmmjTy5Ctezzmlb9zD)
 Call ID: call_p60zSVMmmjTy5Ctezzmlb9zD
  Args:
    summary: Run
    start_datetime: 2025-04-02 19:30:00
    end_datetime: 2025-04-02 20:00:00
    timezone: America/Mexico_City
    color_id: 2
================================= Tool Message =================================
Name: create_calendar_event

Event created: https://www.google.com/calendar/event?eid=czZyZHVpcG43ajNiY241dmJmNWwycjE0NWsgam9yZ2VhbmczM0Bt
================================== Ai Message ==================================

I have created a green event for your run this afternoon. You can view it [in Google Calendar](https://www.google.com/calendar/event?eid=czZyZHVpcG43ajNiY241dmJmNWwycjE0NWsgam9yZ2VhbmczM0Bt). Enjoy your run!
```

***

## API reference

* Refer to the [Google Calendar API overview](https://developers.google.com/calendar/api/guides/overview) for more details from Google Calendar API.
* For detailed documentation of all Google Calendar Toolkit features and configurations head to the [calendar documentation](https://reference.langchain.com/python/langchain-google-community/calendar).

***

[Connect these docs](../../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/python/integrations/tools/google_calendar.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
