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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a054ed08dcee7ecc4105706d38c0b4aa0b3c3c32/libs/langgraph/langgraph/types.py#L493)
