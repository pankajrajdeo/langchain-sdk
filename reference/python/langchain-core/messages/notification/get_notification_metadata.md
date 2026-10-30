---
title: "get_notification_metadata"
description: "Return the notification metadata of message."
source: "https://reference.langchain.com/python/langchain-core/messages/notification/get_notification_metadata"
category: "reference"
tags: [reference, langchain-core, messages, notification, get_notification_metadata]
---

# get_notification_metadata

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/notification/get_notification_metadata)

Return the notification metadata of `message`.

!!! version-added "Added in `langchain-core` 1.7.2"

## Signature

```python
get_notification_metadata(
    message: BaseMessage,
) -> NotificationMetadata | None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `BaseMessage` | Yes | The message to read. |

## Returns

`NotificationMetadata | None`

The metadata `add_notification_metadata` set, or `None` for a message
without a string `lc_source`. `data` is a copy of `lc_data`, left out
unless `lc_data` is a dict.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/messages/notification.py#L72)
