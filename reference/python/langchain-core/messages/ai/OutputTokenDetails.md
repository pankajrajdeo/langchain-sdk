---
title: "OutputTokenDetails"
description: "Breakdown of output token counts."
source: "https://reference.langchain.com/python/langchain-core/messages/ai/OutputTokenDetails"
category: "reference"
tags: [reference, langchain-core, messages, ai, outputtokendetails]
---

# OutputTokenDetails

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/ai/OutputTokenDetails)

Breakdown of output token counts.

Does *not* need to sum to full output token count. Does *not* need to have all keys.

## Signature

```python
OutputTokenDetails()
```

## Description

**Example:**

```python
{
    "audio": 10,
    "reasoning": 200,
}
```

May also hold extra provider-specific keys.

!!! version-added "Added in `langchain-core` 0.3.9"

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    audio: int,
    reasoning: int,
)
```

| Name | Type |
|------|------|
| `audio` | `int` |
| `reasoning` | `int` |

## Properties

- `audio`
- `reasoning`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/messages/ai.py#L74)
