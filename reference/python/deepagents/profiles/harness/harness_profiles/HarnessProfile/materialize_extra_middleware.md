---
title: "materialize_extra_middleware"
description: "Return a fresh list of extra_middleware, invoking factory if supplied."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/materialize_extra_middleware"
category: "reference"
tags: [reference, deepagents, profiles, harness, harness_profiles, harnessprofile, materialize_extra_middleware]
---

# materialize_extra_middleware

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/HarnessProfile/materialize_extra_middleware)

Return a fresh list of `extra_middleware`, invoking factory if supplied.

Each call returns a new list so consumers may mutate freely.

## Signature

```python
materialize_extra_middleware(
    self,
) -> list[AgentMiddleware]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L775)
