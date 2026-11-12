---
title: "ModelCallResult"
description: "Type Alias in langchain"
source: "https://reference.langchain.com/python/langchain/agents/middleware/types/ModelCallResult"
category: "reference"
tags: [reference, langchain, agents, middleware, types, modelcallresult]
---

# ModelCallResult

> **Type Alias** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/types/ModelCallResult)

Return type for model call handlers.

Middleware can return either:

- `ModelResponse`: Full response with messages and optional structured output
- `AIMessage`: Simplified return for simple use cases
- `ExtendedModelResponse`: Response with an optional `Command` for additional state updates
    `goto`, `resume`, and `graph` are not yet supported on these commands.
    A `NotImplementedError` will be raised if you try to use them.

## Signature

```python
ModelCallResult = ModelResponse[ResponseT] | AIMessage | ExtendedModelResponse[ResponseT]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/types.py#L317)
