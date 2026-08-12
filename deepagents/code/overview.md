# Deep Agents Code
> Source: [Original LangChain documentation](https://docs.langchain.com/oss/deepagents/code/overview)
Terminal coding agent built on the Deep Agents SDK

Deep Agents Code (`dcode`) is an open source coding agent built on the [Deep Agents SDK](https://docs.langchain.com/oss/python/deepagents/quickstart).
It works with any large language model and supports switching providers or models.
Persistent memory carries context across conversations, customizable skills shape behavior, and approval controls gate code execution.

## Get started

Run the following command to install Deep Agents Code and launch an interactive session:

```bash
curl -LsSf https://langch.in/dcode | bash
dcode
```

See the [Quickstart](https://docs.langchain.com/oss/deepagents/code/quickstart) to add provider credentials, run your first task, and learn interactive mode.

> **Video:** [Deep Agents Code terminal demo](https://docs.langchain.com/oss/deepagents/code/overview)

## Capabilities

#### [Remote sandboxes](https://docs.langchain.com/oss/deepagents/code/remote-sandboxes)
Run agent tools remotely instead of on your local machine.

#### [Goals and rubrics](https://docs.langchain.com/oss/deepagents/code/goals-and-rubrics)
Define measurable objectives or grading criteria so the agent can check whether work is done.

#### [Subagents](https://docs.langchain.com/oss/deepagents/code/subagents)
Delegate work to task-specific subagents for parallel execution.

#### [Memory](https://docs.langchain.com/oss/deepagents/code/memory-and-skills#memory)
Store and retrieve information across sessions, including project conventions and learned patterns.

#### [Context compaction](https://docs.langchain.com/oss/deepagents/code/quickstart#interactive-mode)
Summarize older messages and offload originals to storage.

#### [Human-in-the-loop](https://docs.langchain.com/oss/deepagents/code/quickstart#interactive-mode)
Require human approval for sensitive tool operations.

#### [Skills](https://docs.langchain.com/oss/deepagents/code/memory-and-skills#skills)
Extend agent capabilities with custom expertise and instructions.

#### [MCP tools](https://docs.langchain.com/oss/deepagents/code/mcp-tools)
Load external tools from Model Context Protocol servers.

#### [Tracing](https://docs.langchain.com/oss/deepagents/code/quickstart#trace-with-langsmith)
Trace agent operations in LangSmith for observability and debugging.

## Next steps

#### [Quickstart](https://docs.langchain.com/oss/deepagents/code/quickstart)
Install Deep Agents Code, run your first task, and use interactive or non-interactive modes.

#### [Configuration](https://docs.langchain.com/oss/deepagents/code/configuration)
Set up credentials, `config.toml`, environment variables, hooks, and CLI flags.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/oss/deepagents/code/overview.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
