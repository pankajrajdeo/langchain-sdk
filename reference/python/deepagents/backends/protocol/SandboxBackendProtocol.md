---
title: "SandboxBackendProtocol"
description: "Extension of BackendProtocol that adds shell command execution."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/SandboxBackendProtocol"
category: "reference"
tags: [reference, deepagents, backends, protocol, sandboxbackendprotocol]
---

# SandboxBackendProtocol

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/SandboxBackendProtocol)

Extension of `BackendProtocol` that adds shell command execution.

Designed for backends running in isolated environments (containers, VMs,
remote hosts).

Adds `execute()`/`aexecute()` for shell commands and an `id` property.

See `BaseSandbox` for a base class that implements all inherited file
operations by delegating to `execute()`.

## Signature

```python
SandboxBackendProtocol()
```

## Extends

- `BackendProtocol`

## Properties

- `id`

## Methods

- [`execute()`](https://reference.langchain.com/python/deepagents/backends/protocol/SandboxBackendProtocol/execute)
- [`aexecute()`](https://reference.langchain.com/python/deepagents/backends/protocol/SandboxBackendProtocol/aexecute)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/protocol.py#L904)
