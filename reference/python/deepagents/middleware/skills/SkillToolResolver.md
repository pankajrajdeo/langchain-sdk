---
title: "SkillToolResolver"
description: "Return the skill tools that one metadata.include_tools name stands for."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillToolResolver"
category: "reference"
tags: [reference, deepagents, middleware, skills, skilltoolresolver]
---

# SkillToolResolver

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillToolResolver)

Return the skill tools that one `metadata.include_tools` name stands for.

A resolver lets a skill list tools whose real names are only known at runtime,
such as generated MCP tool names, and lets one name stand for several tools.
It's called with the name and the graph's `Runtime` on every model call after a
skill listing that name is read, and again before one of its tools runs. It can
be sync or async. An async resolver needs the agent's async entry point, such as
`ainvoke`.

- Return the same tools for the same name within a thread, or the prompt cache
    breaks.
- Keep it cheap, or cache, since it runs on every model call.
- One resolver serves every thread, so scope any cache by what the tools
    depend on, usually something in `runtime.context`.

## Signature

```python
SkillToolResolver = Callable[[str, Runtime[ContextT]], Sequence[BaseTool] | Awaitable[Sequence[BaseTool]]]
```

## Description

**Example:**

```python
# e.g. every tool on a Linear MCP connection, whatever their generated names
tools_by_integration = {"linear": linear_tools}

def resolve_skill_tools(name: str, runtime: Runtime) -> list[BaseTool]:
    return tools_by_integration.get(name, [])

SkillsMiddleware(backend=backend, sources=["/skills/"], tools=resolve_skill_tools)
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/middleware/skills.py#L176)
