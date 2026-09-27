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
    **kwargs: Any = {},
) -> Iterator[T]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `input` | `Iterator[str \| BaseMessage]` | Yes | The input to transform. |
| `config` | `RunnableConfig \| None` | No | The configuration to use for the transformation. (default: `None`) |
| `**kwargs` | `Any` | No | Additional keyword arguments. (default: `{}`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/output_parsers/transform.py#L55)
