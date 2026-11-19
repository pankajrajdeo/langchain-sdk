---
title: "create_checkpoint_plan_for_update_state_api"
description: "Return (channels_to_snapshot, metadata) for an update_state head."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/create_checkpoint_plan_for_update_state_api"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, create_checkpoint_plan_for_update_state_api]
---

# create_checkpoint_plan_for_update_state_api

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/create_checkpoint_plan_for_update_state_api)

Return ``(channels_to_snapshot, metadata)`` for an update_state head.

## Signature

```python
create_checkpoint_plan_for_update_state_api(
    channels: Mapping[str, BaseChannel],
    updated_channels: set[str],
    *,
    source: Literal['update', 'input'],
    step: int,
    parents: dict[str, Any],
    saved_metadata: Mapping[str, Any] | None,
    is_fresh_thread: bool,
    fork_channels: set[str],
    channel_versions: ChannelVersions,
) -> tuple[set[str], dict[str, Any]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/_checkpoint.py#L228)
