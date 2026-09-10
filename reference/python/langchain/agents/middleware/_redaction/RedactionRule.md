---
title: "RedactionRule"
description: "Configuration for handling a single PII type."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/RedactionRule"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, redactionrule]
---

# RedactionRule

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/RedactionRule)

Configuration for handling a single PII type.

## Signature

```python
RedactionRule(
    self,
    pii_type: str,
    strategy: RedactionStrategy = 'redact',
    detector: Detector | str | None = None,
)
```

## Constructors

```python
__init__(
    self,
    pii_type: str,
    strategy: RedactionStrategy = 'redact',
    detector: Detector | str | None = None,
) -> None
```

| Name | Type |
|------|------|
| `pii_type` | `str` |
| `strategy` | `RedactionStrategy` |
| `detector` | `Detector \| str \| None` |

## Properties

- `pii_type`
- `strategy`
- `detector`

## Methods

- [`resolve()`](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/RedactionRule/resolve)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L397)
