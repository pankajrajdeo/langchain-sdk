---
title: "aexecute"
description: "Execute a shell command asynchronously."
source: "https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend/aexecute"
category: "reference"
tags: [reference, deepagents, backends, local_shell, localshellbackend, aexecute]
---

# aexecute

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/local_shell/LocalShellBackend/aexecute)

Execute a shell command asynchronously.

## Signature

```python
aexecute(
    self,
    command: str,
    *,
    timeout: int | None = None,
) -> ExecuteResponse
```

## Description

**Note:**

Cancellation allows synchronous execution a short grace period for
cleanup, set by `_ASYNC_CANCELLATION_GRACE_PERIOD`. Subclasses that
override `execute` retain thread delegation without cancellation
cleanup, even when calling `super().execute`. That bound applies to
this await, not to application shutdown: shutting down the default
executor still waits for running threads.

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `command` | `str` | Yes | Shell command string to execute. |
| `timeout` | `int \| None` | No | Maximum time in seconds to wait for the command. (default: `None`) |

## Returns

`ExecuteResponse`

The command output, exit code, and truncation status.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/backends/local_shell.py#L465)
