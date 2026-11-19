---
title: "user"
description: "The authenticated user, if any."
source: "https://reference.langchain.com/python/langgraph/runtime/ServerInfo/user"
category: "reference"
tags: [reference, langgraph, runtime, serverinfo, user]
---

# user

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/runtime/ServerInfo/user)

The authenticated user, if any.

This implements the `BaseUser` protocol from `langgraph_sdk.auth.types`,
which supports both attribute access (e.g. `user.identity`) and dict-like
access (e.g. `user["identity"]`).

## Signature

```python
user: BaseUser | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/7830b91a24e657a8167e2dbf40c3fa5a77ef5d93/libs/langgraph/langgraph/runtime.py#L70)
