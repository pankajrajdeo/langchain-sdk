---
title: "coerce_timeout_policy"
description: "Normalize a timeout value to positive-second policy fields."
source: "https://reference.langchain.com/python/langgraph/pregel/main/coerce_timeout_policy"
category: "reference"
tags: [reference, langgraph, pregel, main, coerce_timeout_policy]
---

# coerce_timeout_policy

> **Function** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/_internal/_timeout/coerce_timeout_policy)

Normalize a timeout value to positive-second policy fields.

## Signature

```python
coerce_timeout_policy(
    value: float | timedelta | TimeoutPolicy | None,
) -> TimeoutPolicy | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/_internal/_timeout.py#L14)
