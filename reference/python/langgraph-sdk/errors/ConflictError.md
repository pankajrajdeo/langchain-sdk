---
title: "ConflictError"
description: "- APIStatusError"
source: "https://reference.langchain.com/python/langgraph-sdk/errors/ConflictError"
category: "reference"
tags: [reference, langgraph-sdk, errors, conflicterror]
---

# ConflictError

> **Class** in `langgraph_sdk`

📖 [View in docs](https://reference.langchain.com/python/langgraph-sdk/errors/ConflictError)

## Signature

```python
ConflictError(
    self,
    message: str,
    *,
    response: httpx.Response,
    body: object | None,
)
```

## Extends

- `APIStatusError`

## Properties

- `status_code`

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/5db97b9ccab6b8d9a5ab1e8f0bebea7c03a8708a/libs/sdk-py/langgraph_sdk/errors.py#L124)
