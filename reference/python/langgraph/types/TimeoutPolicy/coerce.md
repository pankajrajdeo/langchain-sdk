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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/types.py#L493)
