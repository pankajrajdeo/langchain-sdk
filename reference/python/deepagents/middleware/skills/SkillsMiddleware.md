---
title: "SkillsMiddleware"
description: "Middleware for loading and exposing agent skills to the system prompt."
source: "https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware"
category: "reference"
tags: [reference, deepagents, middleware, skills, skillsmiddleware]
---

# SkillsMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware)

Middleware for loading and exposing agent skills to the system prompt.

Loads skills from backend sources and injects them into the system prompt
using progressive disclosure (metadata first, full content on demand).

Skills are loaded in source order with later sources overriding
earlier ones.

Skills are loaded once per thread and cached in state. To pick up skills
added, edited, or deleted since then, set `skills_metadata` to `None`:

```python
agent.invoke({"messages": messages, "skills_metadata": None}, config)

# or without a run
agent.update_state(config, {"skills_metadata": None})
```

To guarantee the model gets a skill's instructions, for example when the
user names it, pass its name in `pinned_skills`. Before the next model
call, each named skill's `SKILL.md` is appended to the conversation as its
own `HumanMessage`, with `additional_kwargs["lc_source"]` set to
`"pinned_skill"` and the skill's `name`, `path` and `description` under
`additional_kwargs["skill"]`:

```python
agent.invoke(
    {
        "messages": [{"role": "user", "content": "/write-tests /house-style for auth.py"}],
        "pinned_skills": ["write-tests", "house-style"],
    },
    config,
)
```

## Signature

```python
SkillsMiddleware(
    self,
    *,
    backend: BackendProtocol,
    sources: Sequence[SkillSource],
    system_prompt: str | None = SKILLS_SYSTEM_PROMPT,
    tools: Sequence[BaseTool | Callable[..., Any]] | SkillToolResolver | None = None,
)
```

## Description

**Example:**

```python
from deepagents.backends.filesystem import FilesystemBackend

backend = FilesystemBackend(root_dir="/path/to/skills")
middleware = SkillsMiddleware(
    backend=backend,
    sources=[
        "/path/to/skills/user/",
        "/path/to/skills/project/",
        # Pass a (path, label) tuple to disambiguate sources whose
        # leaf directories would otherwise collide
        ("/home/me/.claude/skills", "User Claude"),
        ("/repo/.claude/skills", "Project Claude"),
    ],
)
```

## Skill tools

A skill can list the tools its instructions use, separated by spaces, under
`metadata.include_tools` in its `SKILL.md` frontmatter:

```yaml
metadata:
  include_tools: create_customer_request list_customer_requests
```

Pass those tools as `tools`, either as a list or as a
`SkillToolResolver` that looks them up by name. The model sees a skill tool
only after it uses `read_file` on a skill that lists it, or the skill is
pinned, and only while that read or pinned skill stays in context. Until
then, calling the tool fails as an unknown tool.

`include_tools` can also list a tool passed to the agent rather than to
this middleware. If that tool is deferred
(`extras={"defer_loading": True}`), reading or pinning the skill
discloses it automatically.

## Placement

`create_deep_agent` places this middleware for you. When composing
`create_agent` by hand, include `FilesystemMiddleware`, whose `read_file`
the model uses to read skills. Put this middleware after summarization and
any model fallback or routing middleware, so it sees the compacted
conversation and the model actually called, and before prompt caching:

```python
create_agent(
    model,
    tools=[...],
    middleware=[
        FilesystemMiddleware(backend=backend),
        ...,
        SummarizationMiddleware(...),
        ModelFallbackMiddleware(...),
        SkillsMiddleware(backend=backend, sources=["/skills/"], tools=[...]),
        AnthropicPromptCachingMiddleware(),
    ],
)
```

See constructor for the full argument list.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `backend` | `BackendProtocol` | Yes | Backend instance (e.g. `StateBackend()`). |
| `sources` | `Sequence[SkillSource]` | Yes | List of skill sources.  Each entry is either a bare path (e.g. `'/skills/user/'`) or a `(path, label)` tuple (e.g. `('/home/me/.claude/skills', 'User Claude')`). Labels are rendered as `**{label} Skills**` in the system prompt (do not include the trailing `Skills` in your label). |
| `system_prompt` | `str \| None` | No | System-prompt fragment template. Must contain `{skills_locations}`, `{skills_load_warnings}`, and `{skills_list}` slots for runtime substitution. Pass `None` to skip appending entirely (skills are still loaded into `state["skills_metadata"]`). (default: `SKILLS_SYSTEM_PROMPT`) |
| `tools` | `Sequence[BaseTool \| Callable[..., Any]] \| SkillToolResolver \| None` | No | Tools the model sees only after reading a skill that lists them in `metadata.include_tools`.  A list of tools, or a `SkillToolResolver` that returns the tools for a name. Plain functions in a list are converted to tools, as `create_agent` does. (default: `None`) |

## Extends

- `AgentMiddleware[SkillsState, ContextT, ResponseT]`

## Constructors

```python
__init__(
    self,
    *,
    backend: BackendProtocol,
    sources: Sequence[SkillSource],
    system_prompt: str | None = SKILLS_SYSTEM_PROMPT,
    tools: Sequence[BaseTool | Callable[..., Any]] | SkillToolResolver | None = None,
) -> None
```

| Name | Type |
|------|------|
| `backend` | `BackendProtocol` |
| `sources` | `Sequence[SkillSource]` |
| `system_prompt` | `str \| None` |
| `tools` | `Sequence[BaseTool \| Callable[..., Any]] \| SkillToolResolver \| None` |

## Properties

- `trace_policy`
- `state_schema`
- `sources`
- `source_labels`
- `system_prompt_template`

## Methods

- [`modify_request()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/modify_request)
- [`before_agent()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/before_agent)
- [`abefore_agent()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/abefore_agent)
- [`before_model()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/before_model)
- [`abefore_model()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/abefore_model)
- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/awrap_model_call)
- [`wrap_tool_call()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/wrap_tool_call)
- [`awrap_tool_call()`](https://reference.langchain.com/python/deepagents/middleware/skills/SkillsMiddleware/awrap_tool_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/middleware/skills.py#L916)
