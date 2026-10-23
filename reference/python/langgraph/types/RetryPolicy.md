---
title: "RetryPolicy"
description: "Configuration for retrying nodes."
source: "https://reference.langchain.com/python/langgraph/types/RetryPolicy"
category: "reference"
tags: [reference, langgraph, types, retrypolicy]
---

# RetryPolicy

> **Class** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/RetryPolicy)

Configuration for retrying nodes.

!!! version-added "Added in version 0.2.24"

## Signature

```python
RetryPolicy()
```

## Extends

- `NamedTuple`

## Properties

- `initial_interval`
- `backoff_factor`
- `max_interval`
- `max_attempts`
- `jitter`
- `retry_on`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/types.py#L427)
