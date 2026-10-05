---
title: "before_agent"
description: "Load skills metadata before agent execution (synchronous)."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/before_agent"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware, before_agent]
---

# before_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/before_agent)

Load skills metadata before agent execution (synchronous).

Loads skills from all configured sources when not yet loaded, meaning
`skills_metadata` is missing or `None` in state. If it holds a list
(from a prior turn or checkpointed session, even if empty), the load
is skipped and `None` is returned.

Skills are loaded in source order with later sources overriding
earlier ones if they contain skills with the same name (last one wins).

## Signature

```python
before_agent(
    self,
    state: SkillsState,
    runtime: Runtime,
    config: RunnableConfig,
) -> SkillsStateUpdate | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `state` | `SkillsState` | Yes | Current agent state. |
| `runtime` | `Runtime` | Yes | Runtime context. |
| `config` | `RunnableConfig` | Yes | Runnable config. |

## Returns

`SkillsStateUpdate | None`

State update with `skills_metadata` and `skills_load_errors`, or
`None` if skills are already loaded.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/middleware/skills.py#L949)
