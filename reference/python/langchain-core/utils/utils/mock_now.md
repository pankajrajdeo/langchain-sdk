---
title: "mock_now"
description: "Context manager for mocking out datetime.now() in unit tests."
source: "https://reference.langchain.com/python/langchain-core/utils/utils/mock_now"
category: "reference"
tags: [reference, langchain-core, utils, mock_now]
---

# mock_now

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/utils/mock_now)

Context manager for mocking out datetime.now() in unit tests.

## Signature

```python
mock_now(
    dt_value: datetime.datetime,
) -> Iterator[type]
```

## Description

**Example:**

```python
with mock_now(datetime.datetime(2011, 2, 3, 10, 11)):
    assert datetime.datetime.now() == datetime.datetime(2011, 2, 3, 10, 11)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `dt_value` | `datetime.datetime` | Yes | The datetime value to use for datetime.now(). |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/utils.py#L73)
