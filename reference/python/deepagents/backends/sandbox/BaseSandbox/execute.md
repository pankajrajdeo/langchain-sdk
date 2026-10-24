---
title: "execute"
description: "Execute a command in the sandbox and return ExecuteResponse."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/execute"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, execute]
---

# execute

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/execute)

Execute a command in the sandbox and return `ExecuteResponse`.

## Signature

```python
execute(
    self,
    command: str,
    *,
    timeout: int | None = None,
) -> ExecuteResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `command` | `str` | Yes | Full shell command string to execute. |
| `timeout` | `int \| None` | No | Maximum time in seconds to wait for the command to complete.  If `None`, uses the backend's default timeout. (default: `None`) |

## Returns

`ExecuteResponse`

`ExecuteResponse` with combined output, exit code, and truncation flag.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/sandbox.py#L1631)
