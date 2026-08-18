# Define a Managed Deep Agent

> Configure the model and core capabilities of a Managed Deep Agent.

The agent definition selects the model and core capabilities of a Managed Deep Agent.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Project structure

The agent entry lives at the project root:

```text
my-agent/
  agent.py
```

Export the agent definition as a named `agent`.

## Define an agent

Use `define_deep_agent`:

```python
from managed_deepagents import define_deep_agent

agent = define_deep_agent(
    name="research-assistant",
    model="openai:gpt-5.5",
)
```

```python
from managed_deepagents import define_deep_agent

agent = define_deep_agent(
    name="research-assistant",
    model="anthropic:claude-sonnet-4-6",
)
```

```python
from managed_deepagents import define_deep_agent

agent = define_deep_agent(
    name="research-assistant",
    model="google_genai:gemini-3.6-flash",
)
```

| Parameter                                | What it does                                                          |
| ---------------------------------------- | --------------------------------------------------------------------- |
| [`name=`](#name)                         | Sets the agent and default deployment name                            |
| [`model=`](#model)                       | Selects the chat model                                                |
| [`tools=`](#tools)                       | Adds tools the agent can call                                         |
| [`middleware=`](#middleware)             | Adds behavior around model calls, tool calls, and the agent lifecycle |
| [`subagents=`](#subagents)               | Defines specialized agents for delegated tasks                        |
| [`permissions=`](#permissions)           | Controls path-level access for filesystem tools                       |
| [`interrupt_on=`](#human-in-the-loop)    | Pauses before selected tool calls for human approval                  |
| [`response_format=`](#structured-output) | Defines a structured output schema                                    |

## Name

`name` is required. Pass a static string that starts with a letter and contains only letters, numbers, underscores, or hyphens, such as `"research-assistant"`.

Managed Deep Agents uses the name as the LangGraph assistant ID and the default LangSmith deployment name. You can override the deployment name with `mda deploy --name` without changing the agent definition.

## Model

Set `model` to the chat model the agent uses. The simplest option is a `provider:model` string. Add the provider's API key to `.env` so the model works locally and in the deployment.

```python
from managed_deepagents import define_deep_agent

agent = define_deep_agent(
    name="research-assistant",
    model="openai:gpt-5.5",
)
```

```python
from managed_deepagents import define_deep_agent

agent = define_deep_agent(
    name="research-assistant",
    model="anthropic:claude-sonnet-4-6",
)
```

```python
from managed_deepagents import define_deep_agent

agent = define_deep_agent(
    name="research-assistant",
    model="google_genai:gemini-3.6-flash",
)
```

Pass a LangChain chat model instance instead when you need to configure model parameters in code. For model options and supported providers, see [Models](../../deepagents/models.md).

### Use LLM Gateway

You can use [LLM Gateway](../llm-gateway.md) to control rate limits, fallbacks, and more.

In order to use LLM Gateway, you should:

* Use the ChatOpenAI model directly
* Set a base url of `https://gateway.smith.langchain.com/v1`
* Use your `LANGSMITH_API_KEY` for authentication. Set `LANGSMITH_GATEWAY_API_KEY` only if you need a different key for gateway calls.

```py
import os

from managed_deepagents import define_deep_agent
from langchain_openai import ChatOpenAI

api_key = os.environ.get(
    "LANGSMITH_GATEWAY_API_KEY",
    os.environ.get("LANGSMITH_API_KEY", "missing-langsmith-api-key"),
)
base_url = "https://gateway.smith.langchain.com/v1"

agent = define_deep_agent(
    name="my-agent",
    model=ChatOpenAI(
        model="moonshotai/Kimi-K3",
        api_key=api_key,
        base_url=base_url,
    ),
)
```

> [!NOTE]
> The model slug should be `provider/model-name` when using Gateway. When NOT using Gateway, it is normally `provider:model-name`

In order to scaffold your project to use Gateway from the start, you can pass a `--gateway` flag when initializing your agent:

```bash
mda init my-agent --gateway
```

## Tools

Pass tools in the `tools` list to let the agent call application logic or external services.

Define tools in local modules, import them into the agent entry, and add them to the definition. See [Custom tools](managed-deep-agents-tools.md). To add tools from remote MCP servers without importing them into the agent entry, use [MCP connectors](managed-deep-agents-mcp-connectors.md).

## Middleware

Pass middleware in the `middleware` list to add behavior around model calls, tool calls, and the agent lifecycle. Middleware runs in list order.

See [Custom middleware](managed-deep-agents-middleware.md).

## Subagents

Pass subagent definitions in `subagents` when the agent should delegate specialized or context-heavy work. Each subagent can have its own prompt, model, and tools. See [Subagents](../../deepagents/subagents.md).

## Permissions

Pass filesystem permission rules in `permissions` to control which paths the agent's built-in filesystem tools can read or write. See [Permissions](../../deepagents/permissions.md).

## Human-in-the-loop

Set `interrupt_on` to pause before selected tool calls.

Use this for actions that require a person to approve, edit, or reject the call before it runs. See [Human-in-the-loop](managed-deep-agents-tools.md#human-in-the-loop).

## Structured output

Set `response_format` when the agent must return data that matches a schema instead of an unconstrained text response.

See [Structured output](../../langchain/structured-output.md).

Configure the system prompt, skills, memory, sandbox, identity, channels, and schedules through their project files rather than the agent definition. See [Project structure](managed-deep-agents-project-structure.md).

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-agent-definition.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
