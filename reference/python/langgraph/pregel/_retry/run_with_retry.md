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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/pregel/_retry.py#L573)
