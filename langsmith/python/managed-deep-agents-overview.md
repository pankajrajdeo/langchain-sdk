# Managed Deep Agents
> Source: [Original LangChain documentation](https://docs.langchain.com/langsmith/python/managed-deep-agents-overview)
Overview of Managed Deep Agents public beta features, workflows, and limits.

Managed Deep Agents lets you define an agent as a folder and run it on managed LangSmith infrastructure. You provide the business logic, and Managed Deep Agents provides the agent harness and production infrastructure.

## Define your agent

An agent starts as a project folder that contains the business logic for its behavior:

* **[Instructions](managed-deep-agents-instructions.md)**: The prompt that defines what the agent does and how it behaves.
* **[Tools](managed-deep-agents-tools.md)**: Functions the agent can call to interact with other systems or take actions.
* **[MCP connectors](managed-deep-agents-mcp-connectors.md)**: Remote MCP servers that provide tools to the agent.
* **[Skills](managed-deep-agents-skills.md)**: Reusable, task-specific instructions and resources.

You can add other capabilities as needed. For the complete folder layout, see [Project structure](managed-deep-agents-project-structure.md).

## Run on a managed harness

Managed Deep Agents combines three layers:

* **Your business logic**: The instructions, tools, and skills in your project folder.
* **Agent harness**: The battle-tested [Deep Agents harness](../../deepagents/overview.md) that runs the agent and connects its business logic.
* **Managed infrastructure**: LangSmith infrastructure that operates the agent at scale for production and multi-user applications.

This separation lets you focus on what the agent should do instead of building and operating the systems required to run it.

## Managed infrastructure

The opinionated infrastructure consists of several pieces:

* **Runtime**: [LangSmith Agent Server](../agent-server.md) runs agents in a durable, fault-tolerant manner.
* **Sandboxes**: [LangSmith Sandboxes](../sandboxes.md) let agents write and execute untrusted code in an isolated environment.
* **Evals**: Managed Deep Agents uses [Harbor tasks](managed-deep-agents-evals.md) to test agent behavior.
* **Channels**: The [channels abstraction](managed-deep-agents-channels.md) connects an agent to platforms where its users work.
* **Memory**: [Managed memory](managed-deep-agents-memory.md) lets agents remember information across interactions.
* **Context management**: [LangSmith Context Hub](../use-the-context-hub.md) manages agent instructions and skills. You can update them in the LangSmith UI without redeploying the agent.

To create and deploy an agent, follow the [Managed Deep Agents quickstart](managed-deep-agents-quickstart.md).

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
