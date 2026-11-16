---
title: "log_error_once"
description: "Log an error once."
source: "https://reference.langchain.com/python/langchain-core/tracers/langchain/log_error_once"
category: "reference"
tags: [reference, langchain-core, tracers, langchain, log_error_once]
---

# log_error_once

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/langchain/log_error_once)

Log an error once.

## Signature

```python
log_error_once(
    method: str,
    exception: Exception,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `method` | `str` | Yes | The method that raised the exception. |
| `exception` | `Exception` | Yes | The exception that was raised. |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ea17e48f0a4336c920394fd029de99f1568b4c38/libs/core/langchain_core/tracers/langchain.py#L59)
