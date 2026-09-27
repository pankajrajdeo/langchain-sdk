---
title: "delta_channels_to_snapshot"
description: "Return the set of DeltaChannel names that should snapshot now."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/delta_channels_to_snapshot"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, delta_channels_to_snapshot]
---

# delta_channels_to_snapshot

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/delta_channels_to_snapshot)

Return the set of DeltaChannel names that should snapshot now.

A channel snapshots when EITHER its accumulated update count reaches
`snapshot_frequency` OR the total supersteps since its last snapshot
reaches `DELTA_MAX_SUPERSTEPS_SINCE_SNAPSHOT`. This is a pure
predicate — no mutation.

## Signature

```python
delta_channels_to_snapshot(
    channels: Mapping[str, BaseChannel],
    counters_since_delta_snapshot: Mapping[str, tuple[int, int]],
) -> set[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/49cce0ca852be4cfb567a1cbe0e511ff325a1682/libs/langgraph/langgraph/pregel/_checkpoint.py#L50)
