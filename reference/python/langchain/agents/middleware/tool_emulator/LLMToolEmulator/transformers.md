---
title: "transformers"
description: "Keeps the emulation model call's tokens out of run.messages."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_emulator/LLMToolEmulator/transformers"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_emulator, llmtoolemulator, transformers]
---

# transformers

> **Attribute** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/tool_emulator/LLMToolEmulator/transformers)

Keeps the emulation model call's tokens out of `run.messages`.

Registered only when this middleware is used — see
`InternalCallTransformer` for why the call needs tagging and filtering.

## Signature

```python
transformers = (InternalCallTransformer,)
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d1d95b79213b0212613ae1aa4fad38bea6f1dccf/libs/langchain_v1/langchain/agents/middleware/tool_emulator.py#L73)
