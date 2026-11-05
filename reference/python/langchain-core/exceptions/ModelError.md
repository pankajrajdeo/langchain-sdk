---
title: "ModelError"
description: "Base exception for failures related to model invocation."
source: "https://reference.langchain.com/python/langchain-core/exceptions/ModelError"
category: "reference"
tags: [reference, langchain-core, exceptions, modelerror]
---

# ModelError

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/exceptions/ModelError)

Base exception for failures related to model invocation.

Subclasses correspond to conditions that model providers report consistently,
so the same condition maps to the same exception type regardless of provider.
Most are keyed to the HTTP status they surface it with; `ModelRefusalError`
covers successful responses in which the model refused.

Provider integrations raise HTTP error subclasses that also inherit from the
provider SDK's own exception type, so code catching either continues to work.

## Signature

```python
ModelError()
```

## Extends

- `LangChainException`

## Properties

- `is_retryable`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/b4aa7e7d00c452251720ce30b8bc2c41ca44e1f5/libs/core/langchain_core/exceptions.py#L73)
