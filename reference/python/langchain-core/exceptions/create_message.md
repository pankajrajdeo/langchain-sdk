---
title: "create_message"
description: "Create a message with a link to the LangChain troubleshooting guide."
source: "https://reference.langchain.com/python/langchain-core/exceptions/create_message"
category: "reference"
tags: [reference, langchain-core, exceptions, create_message]
---

# create_message

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/exceptions/create_message)

Create a message with a link to the LangChain troubleshooting guide.

## Signature

```python
create_message(
    *,
    message: str,
    error_code: ErrorCode,
) -> str
```

## Description

**Example:**

```python
create_message(
    message="Failed to parse output",
    error_code=ErrorCode.OUTPUT_PARSING_FAILURE,
)
"Failed to parse output. For troubleshooting, visit: ..."
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `str` | Yes | The message to display. |
| `error_code` | `ErrorCode` | Yes | The error code to display. |

## Returns

`str`

The full message with the troubleshooting link.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/exceptions.py#L143)
