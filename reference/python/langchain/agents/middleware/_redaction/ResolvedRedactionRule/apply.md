---
title: "apply"
description: "Apply this rule to content, returning new content and matches."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/ResolvedRedactionRule/apply"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, resolvedredactionrule, apply]
---

# apply

> **Method** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/ResolvedRedactionRule/apply)

Apply this rule to content, returning new content and matches.

## Signature

```python
apply(
    self,
    content: str,
) -> tuple[str, list[PIIMatch]]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | The text content to scan and redact. |

## Returns

`tuple[str, list[PIIMatch]]`

A tuple of (updated content, list of detected matches).

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/be854a130153e51346d83d3b06f959b80f6cbca6/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L427)
