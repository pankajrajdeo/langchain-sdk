---
title: "coerce"
description: "Normalize a timeout value to positive-second policy fields."
source: "https://reference.langchain.com/python/langgraph/types/TimeoutPolicy/coerce"
category: "reference"
tags: [reference, langgraph, types, timeoutpolicy, coerce]
---

# coerce

> **Method** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/TimeoutPolicy/coerce)

Normalize a timeout value to positive-second policy fields.

## Signature

```python
coerce(
    cls,
    value: float | timedelta | TimeoutPolicy | None,
) -> TimeoutPolicy | None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/types.py#L492)
