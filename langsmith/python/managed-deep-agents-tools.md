# Add custom tools to Managed Deep Agents

> Define authored tools for Managed Deep Agents projects.

Tools add custom capabilities to your agent.

Define LangChain tools in your project, import them into `agent.py`, and pass them to `define_deep_agent`.

To load tools from a remote MCP server instead, use an [MCP connector](managed-deep-agents-mcp-connectors.md).

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Project structure

Keep the agent entry point at the project root and authored tools under `tools/`:

```text
my-agent/
  agent.py
  tools/
    customer.py
```

## Add a tool module

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

## Attach tools to the agent

Import the tools into the project-root agent entry and pass them in the `tools` list.

```python
from managed_deepagents import define_deep_agent

from tools.customer import lookup_customer

agent = define_deep_agent(
    name="support-agent",
    model="openai:gpt-5.5",
    tools=[lookup_customer],
)
```

`mda dev` and `mda deploy` copy the project files into the compiled build.

Your imports should work the same way they do in a normal local Python project.

Use clear, unique tool names to avoid collisions.

## Human-in-the-loop

Pause the agent before sensitive tool calls so a person can approve, edit, or reject them.

Set `interrupt_on` in the agent definition, and optionally set `permissions` to gate tool and filesystem access.

```python
from managed_deepagents import define_deep_agent

from tools.customer import lookup_customer

agent = define_deep_agent(
    name="support-agent",
    model="openai:gpt-5.5",
    tools=[lookup_customer],
    interrupt_on={"lookup_customer": True},
)
```

The `interrupt_on` field applies the same interrupt behavior as LangChain's [human-in-the-loop middleware](../../langchain/guardrails.md#human-in-the-loop).

For decision types (approve, edit, reject), conditional interrupts, and permission rules, see the Deep Agents [Human-in-the-loop](../../deepagents/human-in-the-loop.md) and [Permissions](../../deepagents/permissions.md) guides.

### Respond to an interrupt

When a run hits an interrupt, it pauses and waits for a human response before continuing.

* **During local development**, `mda dev` runs the agent in LangSmith Studio, which surfaces the interrupt so you can inspect the pending tool call and resume the run.
* **On a deployed agent**, resume the paused run through the LangGraph server API with a `Command(resume=...)` payload. See [Human-in-the-loop using server API](../add-human-in-the-loop.md).

> [!NOTE]
> During public beta, Managed Deep Agents is CLI-first and programmatic invocation is not yet documented. To resume runs programmatically from your own application, contact your LangChain team.

Human-in-the-loop needs durable thread state to pause and resume. The managed runtime owns the checkpointer, so no extra setup is required.

## Use secrets and context

Tools can read deployment secrets from environment variables. Put local values in `.env` for `mda dev`; `mda deploy` forwards non-reserved `.env` values as hosted deployment secrets.

For per-run values such as request metadata or feature flags, use the normal LangChain runtime context patterns for tools. See [how to access context from within your tools](../../langchain/tools.md#access-context).

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-tools.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
