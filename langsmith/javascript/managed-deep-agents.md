# Managed Deep Agents

> Build your agent as a directory of files while LangSmith runs the harness and runtime.

Managed Deep Agents (MDA) is the simplest way to build and deploy production agents. You focus on what your agent does. MDA runs it. There are no servers to run and no infrastructure to wire together.

You write the agent's intelligence: its instructions, the tools it can call, the skills it follows and you select the model that drives it. MDA provides everything underneath:

* **The Deep Agents harness**: The agent loop that plans, calls tools, manages a filesystem, and delegates to subagents. See [Deep Agents](https://docs.langchain.com/oss/javascript/deepagents/overview).
* **A managed runtime**: LangSmith Agent Server hosts and operates the agent, and keeps sessions running across restarts.

## Example agent

A managed deep agent, consists of a project folder, which contains the business logic for its behavior:

When you upload this folder with the `mda` CLI, it will automatically run on managed LangSmith infrastructure.
You provide the business logic, and Managed Deep Agents provides the agent harness and production infrastructure.

To get started, see the [Managed Deep Agents quickstart](managed-deep-agents-quickstart.md).

## Core capabilities

Each part of the agent maps to a file or directory. Add the ones your agent needs:

| Capability                                                                            | Path              | Description                                                                              |
| ------------------------------------------------------------------------------------- | ----------------- | ---------------------------------------------------------------------------------------- |
| [Model and configuration](managed-deep-agents-agent-definition.md) | `agent.ts`        | The model and core options. Required.                                                    |
| [Instructions](managed-deep-agents-instructions.md)                | `instructions.md` | The system prompt that defines how the agent behaves.                                    |
| [Skills](managed-deep-agents-skills.md)                            | `skills/`         | Task-specific playbooks the agent loads when they are relevant.                          |
| [Tools](managed-deep-agents-tools.md)                              | `tools/`          | Functions the agent calls to run your application logic or reach external services.      |
| [MCP connectors](managed-deep-agents-mcp-connectors.md)            | `connectors/`     | Remote MCP servers that provide tools to the agent.                                      |
| [Middleware](managed-deep-agents-middleware.md)                    | `middleware/`     | Custom logic that runs around model and tool calls.                                      |
| [Sandbox](managed-deep-agents-sandboxes.md)                        | `sandbox/`        | An isolated filesystem and shell for running agent-written code.                         |
| [Memory](managed-deep-agents-memory.md)                            | `memory.ts`       | Preferences and knowledge that persist across threads.                                   |
| [Identity](managed-deep-agents-identity.md)                        | `identity.ts`     | Per-caller private threads, memory, and credentials for multi-user deployments.          |
| [Channels](managed-deep-agents-channels.md)                        | `channels/`       | Connections to messaging services, such as Slack, that start runs and receive responses. |
| [Schedules](managed-deep-agents-schedules.md)                      | `schedules/`      | Managed cron schedules that run the agent on a recurring basis.                          |
| [Evals](managed-deep-agents-evals.md)                              | `evals/`          | Harbor-style tasks that test the agent.                                                  |

For the full layout, see [Project structure](managed-deep-agents-project-structure.md).

## Next steps

#### [Quickstart](managed-deep-agents-quickstart.md)
Create and deploy your first Managed Deep Agent with the `mda` CLI.

#### [Tutorial](managed-deep-agents-tutorial.md)
Add durable memory and a daily schedule to the quickstart research assistant.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
