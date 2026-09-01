# Managed Deep Agents project structure

> Understand the files and directories in a Managed Deep Agents project.

A Managed Deep Agents project has a required agent entry and optional files that enable managed capabilities.

It is a regular TypeScript project.

> [!NOTE]
> Managed Deep Agents is in **public [beta](../release-stages.md)** and available on [LangSmith Cloud](../cloud.md) in the US region only.

## Project layout

```text
my-agent/
├── agent.ts | agent.tsx            # Core agent definition

├── instructions.md                 # Managed context
├── skills/
│   └── <name>/
│       └── SKILL.md

├── tools/                          # Application code
├── middleware/

├── channels/                       # Managed configuration
│   └── <name>.ts
├── connectors/
│   └── mcp.ts
├── schedules/
│   └── <name>.ts
├── sandbox/
│   └── index.ts
├── identity.ts
├── memory.ts

├── package.json                    # Dependencies and secrets
├── .env

└── evals/                          # Harbor workspace
    ├── harbor-job.json
    └── <task>/                     # Harbor task
        ├── Task.md
        ├── instruction.md
        ├── environment/
        └── tests/
```

The only required file is `agent.ts` or `agent.tsx` at the project root. It must export a named `agent` created with `defineDeepAgent`.

Use only one agent entry in a project. See [Agent definition](managed-deep-agents-agent-definition.md).

## How Managed Deep Agents treats project files

* **Managed context**: `instructions.md` defines the system prompt. Each directory under `skills/` contains task-specific instructions. Managed Deep Agents syncs both to Context Hub.
* **Application code**: Files under `tools/` and `middleware/` are ordinary project modules. Import them from the agent entry. Other local modules work the same way.
* **Managed configuration**: Root `identity.ts` and `memory.ts`, direct children of `channels/`, `connectors/`, and `schedules/`, and `sandbox/index.ts` enable their corresponding capabilities. MCP connector modules export a named `connector`.
* **Dependencies and secrets**: Declare dependencies in `package.json`. Managed Deep Agents loads `.env` locally and forwards eligible values as deployment secrets, but never includes `.env` files in the build archive.
* **Evals**: Managed Deep Agents evals are Harbor evals. Run `mda evals init -i` and develop tasks with a coding agent and the `eval-engineering` skill. Generated runtime files stay under `.mda/evals/` and are not included in the deployed agent build.

The layout above shows the common `.ts` names. TypeScript managed declarations also accept the supported `.tsx`, `.mts`, or `.cts` variants.

***

> [!NOTE]
> [Connect these docs](https://docs.langchain.com/use-these-docs) to Claude, VSCode, and more via MCP for real-time answers.

> [!NOTE]
> [Edit this page on GitHub](https://github.com/langchain-ai/docs/edit/main/src/langsmith/managed-deep-agents-project-structure.mdx) or [file an issue](https://github.com/langchain-ai/docs/issues/new/choose).
