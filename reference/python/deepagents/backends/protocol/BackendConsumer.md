---
title: "BackendConsumer"
description: "Middleware that works on the agent's backend."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/BackendConsumer"
category: "reference"
tags: [reference, deepagents, backends, protocol, backendconsumer]
---

# BackendConsumer

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/BackendConsumer)

Middleware that works on the agent's backend.

`create_deep_agent` calls `bind_backend` on each middleware it is given that
has this method, with the backend its file tools use.

## Signature

```python
BackendConsumer()
```

## Extends

- `Protocol`

## Methods

- [`bind_backend()`](https://reference.langchain.com/python/deepagents/backends/protocol/BackendConsumer/bind_backend)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/backends/protocol.py#L809)
