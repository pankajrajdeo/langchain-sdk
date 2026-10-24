---
title: "execute"
description: "Execute a shell command via the default backend."
source: "https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/execute"
category: "reference"
tags: [reference, deepagents, backends, composite, compositebackend, execute]
---

# execute

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/composite/CompositeBackend/execute)

Execute a shell command via the default backend.

Unlike file operations, execution is not path-routable — it always
delegates to the default backend.

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
| `command` | `str` | Yes | Shell command to execute. |
| `timeout` | `int \| None` | No | Maximum time in seconds to wait for the command to complete.  If `None`, uses the backend's default timeout. (default: `None`) |

## Returns

`ExecuteResponse`

`ExecuteResponse` with output, exit code, and truncation flag.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/composite.py#L814)
