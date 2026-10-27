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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/3521f08e21a7d89c28331191374bc85c11ecb6e2/libs/langgraph/langgraph/types.py#L492)
