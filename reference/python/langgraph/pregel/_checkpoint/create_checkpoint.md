---
title: "create_checkpoint"
description: "Build a new Checkpoint from the previous one and live channel state."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/create_checkpoint"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, create_checkpoint]
---

# create_checkpoint

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/create_checkpoint)

Build a new Checkpoint from the previous one and live channel state.

For each name in `channels_to_snapshot`, a `_DeltaSnapshot(value)` blob
is written into `channel_values[k]`. Other delta channels are omitted
from `channel_values` — the ancestor walk reconstructs their state
from `checkpoint_writes`. Callers compute the set via
`delta_channels_to_snapshot(channels, counters)`; defaults to empty
(no snapshots) when not provided.

`stored_versions` are the channel versions of the last checkpoint the
saver stored. A snapshotted channel whose version has not moved since
then is bumped.

## Signature

```python
create_checkpoint(
    checkpoint: Checkpoint,
    channels: Mapping[str, BaseChannel] | None,
    step: int,
    *,
    id: str | None = None,
    updated_channels: set[str] | None = None,
    get_next_version: GetNextVersion | None = None,
    channels_to_snapshot: set[str] | None = None,
    stored_versions: ChannelVersions | None = None,
    trigger_to_nodes: Mapping[str, Sequence[str]] | None = None,
) -> Checkpoint
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/pregel/_checkpoint.py#L268)
