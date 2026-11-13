---
title: "Add custom tools to Managed Deep Agents"
description: "Define authored tools for managed deep agents projects."
source: "https://docs.langchain.com/langsmith/managed-deep-agents-tools"
category: "docs"
tags: [docs, langsmith, managed-deep-agents-tools]
---

# Add custom tools to Managed Deep Agents

> Define authored tools for managed deep agents projects.

Custom tools are application code the agent can call for fetching real-time data, querying databases, executing code, and taking actions. Unlike [instructions](python/managed-deep-agents-instructions.md) and [skills](python/managed-deep-agents-skills.md), MDA does not discover them automatically.

To load tools from a remote MCP server, see [Connect to MCP servers](python/managed-deep-agents-mcp-connectors.md).

> [!NOTE]
>
> Managed Deep Agents is in **public [beta](release-stages.md)** on [LangSmith Cloud](cloud.md) and [Bring Your Own Cloud (BYOC)](byoc.md). Use Managed Deep Agents CLI and SDK v0.10 or later for BYOC.

Put authored tools under `tools/`, import them into the agent entry, and pass them to the agent definition:

```text
my-agent/
  agent.py
  tools/
    customer.py
```

For the full project layout, see [Project structure](python/managed-deep-agents-project-structure.md).

To load tools from a remote MCP server without importing them into the agent entry, use an [MCP connector](python/managed-deep-agents-mcp-connectors.md) instead.

MCP connectors are declared under `tools/` as well, so the `tools/mcp.py` file name is reserved for that declaration.

## Add a tool

Use authored tools for business logic, private APIs, database access, and other code that belongs in your agent project.

**1. Define a tool module**

**tools/customer.py**

```python
from langchain.tools import tool

@tool(parse_docstring=True)
def lookup_customer(customer_id: str) -> str:
    """Look up a customer record by ID.

    Args:
        customer_id: Customer ID from the CRM.
    """
    return f"Customer {customer_id} is on the enterprise plan."
```

Use clear, unique tool names to avoid collisions. For more about LangChain tool definitions, see [Tools](../langchain/tools.md).

**2. Attach the tool to the agent**

Import the tool into the project-root agent entry and pass it in the `tools` list:

**agent.py**

```python
from managed_deepagents import define_deep_agent

from tools.customer import lookup_customer

agent = define_deep_agent(
    name="support-agent",
    model="openai:gpt-6.1-sol",
    tools=[lookup_customer],
)
```

Your imports should work the same way they do in a normal local Python project.

**3. Add human-in-the-loop (Optional)**

Pause the agent before sensitive tool calls so a person can approve, edit, or reject them.

Set `interrupt_on` in the agent definition, and optionally set `permissions` to gate tool and filesystem access:

**agent.py**

```python
from managed_deepagents import define_deep_agent

from tools.customer import lookup_customer

agent = define_deep_agent(
    name="support-agent",
    model="openai:gpt-6.1-sol",
    tools=[lookup_customer],
    interrupt_on={"lookup_customer": True},
)
```

The `interrupt_on` field applies the same interrupt behavior as LangChain's [human-in-the-loop middleware](../langchain/guardrails.md#human-in-the-loop).

For decision types (approve, edit, reject), conditional interrupts, and permission rules, see the Deep Agents [Human-in-the-loop](../deepagents/human-in-the-loop.md) and [Permissions](../deepagents/permissions.md) guides.

To resume a paused run, see [Respond to an interrupt](#respond-to-an-interrupt).

To pause on a form your own tool posts in Slack instead, see [Agent-owned interrupts](python/managed-deep-agents-agent-owned-interrupts.md).

For a full project that pauses campaign changes for Slack approval, see the [paid media agent template](python/managed-deep-agents-paid-media-agent.md).

## Use secrets and context

A tool reads fixed configuration, such as a region or an endpoint URL, from an environment variable. Put local values in `.env` for `mda dev`. `mda deploy` forwards non-reserved `.env` values as hosted deployment secrets.

Credentials belong in a [connection](python/managed-deep-agents-connections.md) instead. A connection keeps the value in your LangSmith workspace rather than the project. It can also resolve a different credential for each caller. See [Use tools that require authentication](#use-tools-that-require-authentication).

For per-run values such as request metadata or feature flags, see [Access runtime context](#access-runtime-context).

## Deployment

`mda dev` and `mda deploy` copy project files into the compiled build, including modules under `tools/`. Tools are not synced to Context Hub; they ship with the agent code.

## When to use tools

| Concept | Kind | How it reaches the agent |
| - | - | - |
| **Tools** | Application code | Import and pass in the agent definition |
| **[MCP connectors](python/managed-deep-agents-mcp-connectors.md)** | Managed configuration | Declared in the MCP module under `tools/`; no import into the agent entry |
| **[Skills](python/managed-deep-agents-skills.md)** | Managed context | Procedures the agent loads when relevant |
| **[Instructions](python/managed-deep-agents-instructions.md)** | Managed context | Always-on system prompt |

For more information, see [Project structure](python/managed-deep-agents-project-structure.md).

## Respond to an interrupt

When a run hits an interrupt, it pauses and waits for a human response before continuing.

* **During local development**, `mda dev` runs the agent in LangSmith Studio, which surfaces the interrupt so you can inspect the pending tool call and resume the run.
* **On a deployed agent**, resume the paused run through the Agent Server API with a `Command(resume=...)` payload. See [Human-in-the-loop using server API](add-human-in-the-loop.md).

Human-in-the-loop needs durable thread state to pause and resume. The managed runtime owns the checkpointer, so no extra setup is required.

## Use tools that require authentication

If a tool requires an API key or an OAuth token, resolve it at runtime with a [connection](python/managed-deep-agents-connections.md). `connections.get(...)` takes the connection slug and the credential owner, and returns the credential as a string.

The second argument selects the owner. Pass `{"type": "agent"}` for one credential that the whole deployment shares, such as a team search key. Pass `{"type": "user"}` for the calling person's own credential, so the agent acts as them. For more information, see [Choose a credential owner](python/managed-deep-agents-connections.md#choose-a-credential-owner).

This tool resolves the caller's own GitHub credential:

**tools/get_github_user.py**

```python
import httpx
from langchain.tools import tool
from managed_deepagents import connections

@tool
async def get_github_user() -> str:
    """Get the authenticated caller's GitHub login."""
    # Replace `frontend-github` with the name of your connection.
    access_token = await connections.get("frontend-github", {"type": "user"})
    async with httpx.AsyncClient(timeout=30.0) as client:
        response = await client.get(
            "https://api.github.com/user",
            headers={"Authorization": f"Bearer {access_token}"},
        )
        response.raise_for_status()
        return response.json()["login"]
```

A user-owned connection needs a grant from each caller. The first run for someone who has not authorized the service pauses on a [`credential_authorization_required` interrupt](python/managed-deep-agents-connections.md#handle-the-authorization-interrupt). Slack and LangSmith Studio complete that interrupt for the caller.

Create the connection itself with `mda connections create`. For create modes, local development, and the authorization interrupt, see [Manage connections](python/managed-deep-agents-connections.md).

## Access runtime context

For per-run values such as request metadata or feature flags, use the normal LangChain runtime context patterns for tools. See [how to access context from within your tools](../langchain/tools.md#access-context).

For the caller, channel, and sandbox fields that Managed Deep Agents adds, see [Runtime](python/managed-deep-agents-runtime.md).

To read or write files in the thread's sandbox from a tool, use `runtime.backend`. See [Read and write sandbox files from code](python/managed-deep-agents-sandboxes.md#read-and-write-sandbox-files-from-code).

***

[Connect these docs](../use-these-docs.md) to your agent of choice via MCP for real-time answers.

[Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
