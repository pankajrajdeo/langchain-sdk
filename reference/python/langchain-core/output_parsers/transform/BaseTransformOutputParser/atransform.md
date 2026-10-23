---
title: "atransform"
description: "Async transform the input into the output format."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/transform/BaseTransformOutputParser/atransform"
category: "reference"
tags: [reference, langchain-core, output_parsers, transform, basetransformoutputparser, atransform]
---

# atransform

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/transform/BaseTransformOutputParser/atransform)

Async transform the input into the output format.

## Signature

```python
atransform(
    self,
    input: AsyncIterator[str | BaseMessage],
    config: RunnableConfig | None = None,
    kwargs: Any = {},
) -> AsyncIterator[T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `AsyncIterator[str \| BaseMessage]` | Yes | The input to transform. |
| `config` | `RunnableConfig \| None` | No | The configuration to use for the transformation. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/output_parsers/transform.py#L76)
