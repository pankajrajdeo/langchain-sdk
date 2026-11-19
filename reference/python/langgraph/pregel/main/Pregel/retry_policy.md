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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/pregel/main.py#L828)
