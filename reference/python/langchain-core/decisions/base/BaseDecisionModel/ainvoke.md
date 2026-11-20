---
title: "ainvoke"
description: "Classify one request asynchronously."
source: "https://reference.langchain.com/python/langchain-core/decisions/base/BaseDecisionModel/ainvoke"
category: "reference"
tags: [reference, langchain-core, decisions, base, basedecisionmodel, ainvoke]
---

# ainvoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/base/BaseDecisionModel/ainvoke)

Classify one request asynchronously.

## Signature

```python
ainvoke(
    self,
    input: ClassifierRequest,
    config: RunnableConfig | None = None,
    _: Any = {},
) -> ClassifierResponse
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `ClassifierRequest` | Yes | State and questions to evaluate. |
| `config` | `RunnableConfig \| None` | No | Optional runnable configuration for callbacks, tags, metadata, and tracing. (default: `None`) |
| `**_` | `Any` | No | Accepted for `Runnable` compatibility and otherwise ignored. (default: `{}`) |

## Returns

`ClassifierResponse`

Typed answers keyed by answer ID, with request metadata.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/decisions/base.py#L122)
