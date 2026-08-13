# Add instructions to Managed Deep Agents

> Define the system prompt for a Managed Deep Agent in instructions.md.

Instructions define the agent's behavior. They make up the core of the agent's system prompt. You can define them in a simple markdown file and they are picked up automatically by the agent.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Project structure

The `instructions.md` file lives at the project root:

```text
my-agent/
  agent.py
  instructions.md
```

## Add instructions

Create or modify `instructions.md`:

```markdown
# Assistant

You are a helpful assistant.
```

Use this file to define the agent's role, behavior, constraints, and guidance for using its tools.

## How the agent uses instructions

Instructions are inserted into the agents system prompt on every run. They are always present and help guide the agents behavior.

## Syncing to Context Hub

When you run `mda deploy` to deploy the agent, instructions are automatically synced to the agent's [Context Hub](../use-the-context-hub.md) repo. You can then edit the instructions in the LangSmith UI and have your changes automatically propagated to the agent.

## How instructions compare to other concepts

Use [skills](managed-deep-agents-skills.md) for task-specific procedures that the agent loads only when relevant. Use [memory](managed-deep-agents-memory.md) for knowledge the agent learns and retains across threads.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-instructions.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
