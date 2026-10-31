---
title: "is_prefix_match"
description: "Whether event_namespace starts with prefix."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/subscription/is_prefix_match"
category: "reference"
tags: [reference, langgraph-sdk, stream, subscription, is_prefix_match]
---

# is_prefix_match

> **Function** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/subscription/is_prefix_match)

Whether `event_namespace` starts with `prefix`.

Segments compare literally first; if the prefix segment contains no `:`,
the candidate is also compared after its dynamic suffix is stripped.
Mirrors `is_prefix_match` in `api/langgraph_api/protocol/namespace.py`.

## Signature

```python
is_prefix_match(
    event_namespace: Namespace,
    prefix: Namespace,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5bd231cbfd913e05ebc662f519eb9a655bc766df/libs/sdk-py/langgraph_sdk/stream/subscription.py#L19)
