---
title: "apply_strategy"
description: "Apply the configured strategy to matches within content."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/apply_strategy"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, apply_strategy]
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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L306)
