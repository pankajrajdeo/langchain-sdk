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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/sdk-py/langgraph_sdk/stream/subscription.py#L39)
