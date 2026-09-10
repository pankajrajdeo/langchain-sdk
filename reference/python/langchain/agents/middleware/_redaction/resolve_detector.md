---
title: "resolve_detector"
description: "Return a callable detector for the given configuration."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/resolve_detector"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, resolve_detector]
---

# resolve_detector

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/resolve_detector)

Return a callable detector for the given configuration.

## Signature

```python
resolve_detector(
    pii_type: str,
    detector: Detector | str | None,
) -> Detector
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `pii_type` | `str` | Yes | The PII type name. |
| `detector` | `Detector \| str \| None` | Yes | Optional custom detector or regex pattern. If `None`, a built-in detector for the given PII type will be used. |

## Returns

`Detector`

The resolved detector.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/79cab2dc7f58be720cac43db3677b4c1fd971f91/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L339)
