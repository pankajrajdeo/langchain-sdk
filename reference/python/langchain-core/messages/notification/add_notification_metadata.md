---
title: "add_notification_metadata"
description: "Return a copy of message marked as added by the agent harness."
source: "https://reference.langchain.com/python/langchain-core/messages/notification/add_notification_metadata"
category: "reference"
tags: [reference, langchain-core, messages, notification, add_notification_metadata]
---

# add_notification_metadata

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/messages/notification/add_notification_metadata)

Return a copy of `message` marked as added by the agent harness.

Use it for a human message the user didn't type, such as a background task
update or a conversation summary. It sets `additional_kwargs["lc_source"]`
and, when `data` is given, `additional_kwargs["lc_data"]`. Any earlier
`lc_source` and `lc_data` are removed first. LangChain's chat model
integrations don't send these keys to the model.

It doesn't change the content. Write the content the model reads yourself.

Anyone who can send input to a thread can set these keys. Don't use them to
decide whether to trust a message.

`merge_message_runs` and chunk addition join a notification with adjacent
human messages; the merged message keeps the metadata and concatenates
`lc_source`.

!!! version-added "Added in `langchain-core` 1.7.2"

## Signature

```python
add_notification_metadata(
    message: HumanMessage,
    *,
    source: str,
    data: dict[str, Any] | None = None,
) -> HumanMessage
```

## Description

**Example:**

```python
from langchain_core.messages import HumanMessage, add_notification_metadata

message = add_notification_metadata(
    HumanMessage("Background task t_42 finished."),
    source="async_subagent",
    data={"task_id": "t_42", "status": "success"},
)
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `message` | `HumanMessage` | Yes | The message to mark. |
| `source` | `str` | Yes | The feature that added the message. |
| `data` | `dict[str, Any] \| None` | No | The feature's fields. Must be JSON-serializable. (default: `None`) |

## Returns

`HumanMessage`

A shallow copy of `message`, with the same `id`.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/messages/notification.py#L24)
