---
title: "aparse_result"
description: "Parse a list of candidate model Generation objects into a specific format."
source: "https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/aparse_result"
category: "reference"
tags: [reference, langchain-core, output_parsers, base, baseoutputparser, aparse_result]
---

# aparse_result

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/output_parsers/base/BaseOutputParser/aparse_result)

Parse a list of candidate model `Generation` objects into a specific format.

The return value is parsed from only the first `Generation` in the result, which
is assumed to be the highest-likelihood `Generation`.

This method is used by `ainvoke` and `abatch`. The default implementation
runs `parse_result` in an executor; it does not call `aparse`. Override this
method to provide native async parsing, for example when using async I/O or
clients bound to the caller's event loop. Synchronous parsers can use the
default implementation.

## Signature

```python
aparse_result(
    self,
    result: list[Generation],
    *,
    partial: bool = False,
) -> T
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `result` | `list[Generation]` | Yes | A list of `Generation` to be parsed.  The `Generation` objects are assumed to be different candidate outputs for a single model input. |
| `partial` | `bool` | No | Whether to parse the output as a partial result.  This is useful for parsers that can parse partial results. (default: `False`) |

## Returns

`T`

Structured output.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/2b7ff14fb2021e6f4ee22f796a9b888eaacb5af9/libs/core/langchain_core/output_parsers/base.py#L281)
