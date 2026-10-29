---
title: "transform"
description: "Transform the input into the output format."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/transform/BaseTransformOutputParser/transform"
category: "reference"
tags: [reference, langchain-core, output_parsers, transform, basetransformoutputparser]
---

# transform

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/transform/BaseTransformOutputParser/transform)

Transform the input into the output format.

## Signature

```python
transform(
    self,
    input: Iterator[str | BaseMessage],
    config: RunnableConfig | None = None,
    kwargs: Any = {},
) -> Iterator[T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Iterator[str \| BaseMessage]` | Yes | The input to transform. |
| `config` | `RunnableConfig \| None` | No | The configuration to use for the transformation. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/output_parsers/transform.py#L55)
