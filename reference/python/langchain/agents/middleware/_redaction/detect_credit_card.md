---
title: "detect_credit_card"
description: "Detect credit card numbers in content using Luhn validation."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_credit_card"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, detect_credit_card]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L71)
