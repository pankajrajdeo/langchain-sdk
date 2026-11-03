---
title: "NotificationMetadata"
description: "Which feature added a message, and that feature's fields."
source: "https://reference.langchain.com/python/langchain-core/messages/notification/NotificationMetadata"
category: "reference"
tags: [reference, langchain-core, messages, notification, notificationmetadata]
---

# NotificationMetadata

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/notification/NotificationMetadata)

Which feature added a message, and that feature's fields.

!!! version-added "Added in `langchain-core` 1.7.2"

## Signature

```python
NotificationMetadata()
```

## Extends

- `TypedDict`

## Constructors

```python
__init__(
    source: str,
    data: NotRequired[dict[str, Any]],
)
```

| Name | Type |
|------|------|
| `source` | `str` |
| `data` | `NotRequired[dict[str, Any]]` |

## Properties

- `source`
- `data`

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/e936943647fe9bd9c4c24122ee3e1812ead82130/libs/core/langchain_core/messages/notification.py#L11)
