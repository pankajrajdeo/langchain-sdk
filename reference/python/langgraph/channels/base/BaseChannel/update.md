---
title: "update"
description: "Update the channel's value with the given sequence of updates. The order of the updates in the sequence is arbitrary. This method is called by Pregel for all channels at the end of each step."
source: "https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/update"
category: "reference"
tags: [reference, langgraph, channels, base, basechannel, update]
---

# update

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/channels/base/BaseChannel/update)

Update the channel's value with the given sequence of updates.
The order of the updates in the sequence is arbitrary.
This method is called by Pregel for all channels at the end of each step.

If there are no updates, it is called with an empty sequence.

Raises `InvalidUpdateError` if the sequence of updates is invalid.

Returns `True` if the channel was updated, `False` otherwise.

## Signature

```python
update(
    self,
    values: Sequence[Update],
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/channels/base.py#L89)
