---
title: "delta_channels_overwritten"
description: "Return the names of the DeltaChannels that writes set with an Overwrite."
source: "https://reference.langchain.com/python/langgraph/pregel/_checkpoint/delta_channels_overwritten"
category: "reference"
tags: [reference, langgraph, pregel, checkpoint, delta_channels_overwritten]
---

# delta_channels_overwritten

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/delta_channels_overwritten)

Return the names of the DeltaChannels that `writes` set with an `Overwrite`.

`update_state` saves a full snapshot of these channels in the checkpoint it
creates, like the loop does when a node returns an `Overwrite`. Otherwise,
reading the channel later starts from an older snapshot and replays the
writes the `Overwrite` threw away.

## Signature

```python
delta_channels_overwritten(
    specs: Mapping[str, Any],
    writes: Iterable[tuple[str, Any]],
) -> set[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/_checkpoint.py#L157)
