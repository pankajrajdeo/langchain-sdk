---
title: "sanitize_untracked_values_in_send"
description: "Pop any values belonging to UntrackedValue channels in Send.arg for safe checkpointing."
source: "https://reference.langchain.com/python/langgraph/pregel/_algo/sanitize_untracked_values_in_send"
category: "reference"
tags: [reference, langgraph, pregel, algo, sanitize_untracked_values_in_send]
---

# sanitize_untracked_values_in_send

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_algo/sanitize_untracked_values_in_send)

Pop any values belonging to UntrackedValue channels in Send.arg for safe checkpointing.

Send is often called with state to be passed to the dest node, which may contain
UntrackedValues at the top level. Send is not typed and arg may be a nested dict.

## Signature

```python
sanitize_untracked_values_in_send(
    packet: Send,
    channels: Mapping[str, BaseChannel],
) -> Send
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/pregel/_algo.py#L1447)
