---
title: "ResolvedRedactionRule"
description: "Resolved redaction rule ready for execution."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/ResolvedRedactionRule"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, resolvedredactionrule]
---

# ResolvedRedactionRule

> **Class** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/ResolvedRedactionRule)

Resolved redaction rule ready for execution.

## Signature

```python
ResolvedRedactionRule(
    self,
    pii_type: str,
    strategy: RedactionStrategy,
    detector: Detector,
)
```

## Constructors

```python
__init__(
    self,
    pii_type: str,
    strategy: RedactionStrategy,
    detector: Detector,
) -> None
```

| Name | Type |
|------|------|
| `pii_type` | `str` |
| `strategy` | `RedactionStrategy` |
| `detector` | `Detector` |

## Properties

- `pii_type`
- `strategy`
- `detector`

## Methods

- [`apply()`](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/ResolvedRedactionRule/apply)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L419)
