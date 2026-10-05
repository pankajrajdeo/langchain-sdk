---
title: "elapsed"
description: "Get the elapsed time of a run."
source: "https://reference.langchain.com/python/langchain-core/tracers/stdout/elapsed"
category: "reference"
tags: [reference, langchain-core, tracers, stdout, elapsed]
---

# elapsed

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/stdout/elapsed)

Get the elapsed time of a run.

## Signature

```python
elapsed(
    run: Any,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `run` | `Any` | Yes | any object with a `start_time` and `end_time` attribute. |

## Returns

`str`

A string with the elapsed time in seconds or milliseconds if time is less than a
second.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/04ac76c07ec173a44e3e57de54861d0b637e3299/libs/core/langchain_core/tracers/stdout.py#L30)
