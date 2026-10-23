---
title: "retry_policy"
description: "Retry policies to use when running tasks. Empty set disables retries."
source: "https://reference.langchain.com/python/langgraph/pregel/main/Pregel/retry_policy"
category: "reference"
tags: [reference, langgraph, pregel, main, retry_policy]
---

# retry_policy

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/main/Pregel/retry_policy)

Retry policies to use when running tasks. Empty set disables retries.

## Signature

```python
retry_policy: Sequence[RetryPolicy] = (retry_policy,) if isinstance(retry_policy, RetryPolicy) else retry_policy
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/41c9c22fdc83d68a2859d0c9a2b627c8615a792f/libs/langgraph/langgraph/pregel/main.py#L832)
