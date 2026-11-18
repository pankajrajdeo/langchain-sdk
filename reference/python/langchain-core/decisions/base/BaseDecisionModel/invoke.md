---
title: "invoke"
description: "Classify one request synchronously."
source: "https://reference.langchain.com/python/langchain-core/decisions/base/BaseDecisionModel/invoke"
category: "reference"
tags: [reference, langchain-core, decisions, base, basedecisionmodel, invoke]
---

# invoke

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/decisions/base/BaseDecisionModel/invoke)

Classify one request synchronously.

## Signature

```python
invoke(
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/5069b326c53069ec85a7e1d914c6873feb8d0cfa/libs/core/langchain_core/decisions/base.py#L97)
