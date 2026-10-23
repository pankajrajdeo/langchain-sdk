---
title: "versions_seen_without_bumps"
description: "versions_seen as the nodes read it: an entry a bump advanced goes back to the version the node really read, or away if it never read one."
source: "https://reference.langchain.com/python/langgraph/pregel/main/versions_seen_without_bumps"
category: "reference"
tags: [reference, langgraph, pregel, main, versions_seen_without_bumps]
---

# versions_seen_without_bumps

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_checkpoint/versions_seen_without_bumps)

`versions_seen` as the nodes read it: an entry a bump advanced goes back
to the version the node really read, or away if it never read one.

## Signature

```python
versions_seen_without_bumps(
    versions_seen: dict[str, ChannelVersions],
) -> dict[str, ChannelVersions]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/_checkpoint.py#L389)
