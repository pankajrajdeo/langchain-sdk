---
title: "execute_accepts_timeout"
description: "Check whether a backend class's execute accepts a timeout kwarg."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/execute_accepts_timeout"
category: "reference"
tags: [reference, deepagents, backends, protocol, execute_accepts_timeout]
---

# execute_accepts_timeout

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/execute_accepts_timeout)

Check whether a backend class's `execute` accepts a `timeout` kwarg.

Older backend packages didn't lower-bound their SDK dependency, so they
may not accept the `timeout` keyword added to
[`SandboxBackendProtocol`][deepagents.backends.protocol.SandboxBackendProtocol].

Results are cached per class to avoid repeated introspection overhead.

## Signature

```python
execute_accepts_timeout(
    cls: type[SandboxBackendProtocol],
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/protocol.py#L968)
