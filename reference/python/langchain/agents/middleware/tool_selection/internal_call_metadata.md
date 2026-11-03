---
title: "internal_call_metadata"
description: "Return metadata that marks a model call as internal to middleware."
source: "https://reference.langchain.com/python/langchain/agents/middleware/tool_selection/internal_call_metadata"
category: "reference"
tags: [reference, langchain, agents, middleware, tool_selection, internal_call_metadata]
---

# internal_call_metadata

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/internal_call_transformer/internal_call_metadata)

Return metadata that marks a model call as internal to middleware.

## Signature

```python
internal_call_metadata() -> dict[str, Any]
```

## Returns

`dict[str, Any]`

A mapping to merge into a model call's `config["metadata"]`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5dcec1858191a6b54cd843dd8e54d856e2e007cc/libs/langchain_v1/langchain/agents/middleware/internal_call_transformer.py#L34)
