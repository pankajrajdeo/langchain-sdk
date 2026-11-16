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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/tracers/stdout.py#L30)
