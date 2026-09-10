---
title: "ShellSession"
description: "Persistent shell session that supports sequential command execution."
source: "https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellSession"
category: "reference"
tags: [reference, langchain, agents, middleware, shell_tool, shellsession]
---

# ShellSession

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellSession)

Persistent shell session that supports sequential command execution.

## Signature

```python
ShellSession(
    self,
    workspace: Path,
    policy: BaseExecutionPolicy,
    command: tuple[str, ...],
    environment: Mapping[str, str],
)
```

## Constructors

```python
__init__(
    self,
    workspace: Path,
    policy: BaseExecutionPolicy,
    command: tuple[str, ...],
    environment: Mapping[str, str],
) -> None
```

| Name | Type |
|------|------|
| `workspace` | `Path` |
| `policy` | `BaseExecutionPolicy` |
| `command` | `tuple[str, ...]` |
| `environment` | `Mapping[str, str]` |

## Methods

- [`start()`](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellSession/start)
- [`restart()`](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellSession/restart)
- [`stop()`](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellSession/stop)
- [`execute()`](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/ShellSession/execute)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L125)
