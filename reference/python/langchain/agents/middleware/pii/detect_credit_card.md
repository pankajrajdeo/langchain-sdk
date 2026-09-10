---
title: "detect_credit_card"
description: "Detect credit card numbers in content using Luhn validation."
source: "https://reference.langchain.com/python/langchain/agents/middleware/pii/detect_credit_card"
category: "reference"
tags: [reference, langchain, agents, middleware, pii, detect_credit_card]
---

# detect_credit_card

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_credit_card)

Detect credit card numbers in content using Luhn validation.

## Signature

```python
detect_credit_card(
    content: str,
) -> list[PIIMatch]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | The text content to scan for credit card numbers. |

## Returns

`list[PIIMatch]`

A list of detected credit card matches.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L71)
