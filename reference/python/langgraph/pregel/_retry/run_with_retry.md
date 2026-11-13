---
title: "run_with_retry"
description: "Run a task with retries."
source: "https://reference.langchain.com/python/langgraph/pregel/_retry/run_with_retry"
category: "reference"
tags: [reference, langgraph, pregel, retry, run_with_retry]
---

# run_with_retry

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/pregel/_retry/run_with_retry)

Run a task with retries.

## Signature

```python
run_with_retry(
    task: PregelExecutableTask,
    retry_policy: Sequence[RetryPolicy] | None,
    configurable: dict[str, Any] | None = None,
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/pregel/_retry.py#L593)
