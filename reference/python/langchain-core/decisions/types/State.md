---
title: "State"
description: "Type Alias in langchain_core"
source: "https://reference.langchain.com/python/langchain-core/decisions/types/State"
category: "reference"
tags: [reference, langchain-core, decisions, types, state]
---

# State

> **Type Alias** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/types/State)

Root state accepted by decision models.

State is a string, JSON object, or JSON array. LangChain `BaseMessage` objects and
message sequences can appear at the root or at any depth inside objects and arrays.
LangChain standard media blocks (for example `{"type": "image", "base64": ...,
"mime_type": ...}`) may appear anywhere in the state. Each provider documents which
media it supports and how it sends state its API cannot accept natively.

## Signature

```python
State: TypeAlias = str | BaseMessage | Sequence[_StateValue] | Mapping[str, _StateValue]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/decisions/types.py#L32)
