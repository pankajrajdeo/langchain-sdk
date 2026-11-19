---
title: "detect_mac_address"
description: "Detect MAC addresses in content."
source: "https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_mac_address"
category: "reference"
tags: [reference, langchain, agents, middleware, redaction, detect_mac_address]
---

# detect_mac_address

> **Function** in `langchain`

📖 [View in docs](https://reference.langchain.com/python/langchain/agents/middleware/_redaction/detect_mac_address)

Detect MAC addresses in content.

## Signature

```python
detect_mac_address(
    content: str,
) -> list[PIIMatch]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `content` | `str` | Yes | The text content to scan for MAC addresses. |

## Returns

`list[PIIMatch]`

A list of detected MAC address matches.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/ced9bdb1a8899516b6c541fc0e19ab5f349aa0ea/libs/langchain_v1/langchain/agents/middleware/_redaction.py#L128)
