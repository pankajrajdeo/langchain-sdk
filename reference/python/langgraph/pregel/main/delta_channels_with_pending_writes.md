---
title: "delta_channels_with_pending_writes"
description: "DeltaChannels a branch starting from this checkpoint must snapshot."
source: "https://reference.langchain.com/python/langgraph/pregel/main/delta_channels_with_pending_writes"
category: "reference"
tags: [reference, langgraph, pregel, main, delta_channels_with_pending_writes]
---

# delta_channels_with_pending_writes

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/delta_channels_with_pending_writes)

DeltaChannels a branch starting from this checkpoint must snapshot.

A checkpoint's pending writes belong to the child that consumed them, and
nothing records which child that was. A new branch snapshots every delta
channel they touch, so its ancestor walk never replays them.

## Signature

```python
delta_channels_with_pending_writes(
    specs: Mapping[str, Any],
    pending_writes: Iterable[PendingWrite] | None,
) -> set[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/pregel/_checkpoint.py#L140)
