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

Loads skills once per session from all configured sources. If
`skills_metadata` is already present in state (from a prior turn or
checkpointed session), the load is skipped and `None` is returned.

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

State update with `skills_metadata` populated, or `None` if already present.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/skills.py#L933)
