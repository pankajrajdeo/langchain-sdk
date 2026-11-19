---
title: "delta_channels_overwritten"
description: "Return the names of the DeltaChannels that writes set with an Overwrite."
source: "https://reference.langchain.com/python/langgraph/pregel/main/delta_channels_overwritten"
category: "reference"
tags: [reference, langgraph, pregel, main, delta_channels_overwritten]
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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/_checkpoint.py#L157)
