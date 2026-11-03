---
title: "CommandExecutionResult"
description: "Structured result from command execution."
source: "https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/CommandExecutionResult"
category: "reference"
tags: [reference, langchain, agents, middleware, shell_tool, commandexecutionresult]
---

# CommandExecutionResult

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/shell_tool/CommandExecutionResult)

Structured result from command execution.

## Signature

```python
CommandExecutionResult(
    self,
    output: str,
    exit_code: int | None,
    timed_out: bool,
    truncated_by_lines: bool,
    truncated_by_bytes: bool,
    total_lines: int,
    total_bytes: int,
)
```

## Constructors

```python
__init__(
    self,
    output: str,
    exit_code: int | None,
    timed_out: bool,
    truncated_by_lines: bool,
    truncated_by_bytes: bool,
    total_lines: int,
    total_bytes: int,
) -> None
```

| Name | Type |
|------|------|
| `output` | `str` |
| `exit_code` | `int \| None` |
| `timed_out` | `bool` |
| `truncated_by_lines` | `bool` |
| `truncated_by_bytes` | `bool` |
| `total_lines` | `int` |
| `total_bytes` | `int` |

## Properties

- `output`
- `exit_code`
- `timed_out`
- `truncated_by_lines`
- `truncated_by_bytes`
- `total_lines`
- `total_bytes`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/agents/middleware/shell_tool.py#L112)
