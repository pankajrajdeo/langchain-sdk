---
title: "ensure_message_ids"
description: "Give the messages written to DeltaChannels stable ids."
source: "https://reference.langchain.com/python/langgraph/pregel/_messages/ensure_message_ids"
category: "reference"
tags: [reference, langgraph, pregel, messages, ensure_message_ids]
---

# ensure_message_ids

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_messages/ensure_message_ids)

Give the messages written to DeltaChannels stable ids.

A `DeltaChannel` replays its saved writes on every read, and its reducer
may not assign missing ids (`_messages_delta_reducer` doesn't), so a
message saved without an id comes back without one, or with a new one on
every read, and nothing can target it by id, for example `RemoveMessage`.

In a channel whose reducer is `_messages_delta_reducer`, every message-like
it accepts (a message, a dict, a string, a `(role, content)` tuple; alone,
in a list or in an `Overwrite`) becomes a message with an id. Other
DeltaChannels may hold other data, so there only message objects get ids,
plus message dicts outside an `Overwrite`: one in a list becomes a message.
Anything that can't become a message is left as it is, so it fails where
it always has: a message dict in a list raises here, anything else when
the reducer reads it. An empty id counts as missing.

A write that changes is replaced in `writes`: lists and dicts the caller
passed in are never changed, only the ids of message objects.

## Signature

```python
ensure_message_ids(
    channels: Mapping[str, Any],
    writes: Sequence[tuple[str, Any]],
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/_messages.py#L503)
