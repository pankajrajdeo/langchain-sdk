---
title: "namespace_matches"
description: "Whether event_namespace matches any of prefixes within depth."
source: "https://reference.langchain.com/python/langgraph-sdk/stream/subscription/namespace_matches"
category: "reference"
tags: [reference, langgraph-sdk, stream, subscription, namespace_matches]
---

# namespace_matches

> **Function** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/stream/subscription/namespace_matches)

Whether `event_namespace` matches any of `prefixes` within `depth`.

## Signature

```python
namespace_matches(
    event_namespace: Namespace,
    prefixes: list[Namespace] | None,
    depth: int | None,
) -> bool
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/6b83b9b019c9b2680e4456dd6835d0fea27b9887/libs/sdk-py/langgraph_sdk/stream/subscription.py#L39)
