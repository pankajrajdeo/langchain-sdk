---
title: "apply_strategy"
description: "Apply the configured strategy to matches within content."
source: "https://reference.langchain.com/python/langchain/agents/middleware/pii/apply_strategy"
category: "reference"
tags: [reference, langchain, agents, middleware, pii, apply_strategy]
---

# apply_strategy

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/apply_strategy)

Apply the configured strategy to matches within content.

## Signature

```python
apply_strategy(
    content: str,
    matches: list[PIIMatch],
    strategy: RedactionStrategy,
) -> str
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | The content to apply strategy to. |
| `matches` | `list[PIIMatch]` | Yes | List of detected PII matches. |
| `strategy` | `RedactionStrategy` | Yes | The redaction strategy to apply. |

## Returns

`str`

The content with the strategy applied.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L306)
