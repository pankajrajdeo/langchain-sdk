---
title: "detect_url"
description: "Detect URLs in content using regex and stdlib validation."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_url"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, detect_url]
---

# detect_url

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_url)

Detect URLs in content using regex and stdlib validation.

## Signature

```python
detect_url(
    content: str,
) -> list[PIIMatch]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | The text content to scan for URLs. |

## Returns

`list[PIIMatch]`

A list of detected URL matches.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c2f4036e4c6ca45a8da8a42d8e07a25d2ea48b8f/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L149)
