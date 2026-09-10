---
title: "uuid7"
description: "Generate a UUID from a Unix timestamp in nanoseconds and random bits."
source: "https://reference.langchain.com/python/langchain-core/utils/uuid/uuid7"
category: "reference"
tags: [reference, langchain-core, utils, uuid, uuid7]
---

# uuid7

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/utils/uuid/uuid7)

Generate a UUID from a Unix timestamp in nanoseconds and random bits.

UUIDv7 objects feature monotonicity within a millisecond.

## Signature

```python
uuid7(
    nanoseconds: int | None = None,
) -> UUID
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `nanoseconds` | `int \| None` | No | Optional ns timestamp. If not provided, uses current time. (default: `None`) |

## Returns

`UUID`

A UUIDv7 object.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/utils/uuid.py#L26)
