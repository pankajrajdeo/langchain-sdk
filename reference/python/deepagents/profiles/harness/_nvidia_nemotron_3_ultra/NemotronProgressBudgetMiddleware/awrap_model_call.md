---
title: "awrap_model_call"
description: "Async variant of wrap_model_call."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronProgressBudgetMiddleware/awrap_model_call"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, nemotronprogressbudgetmiddleware, awrap_model_call]
---

# awrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronProgressBudgetMiddleware/awrap_model_call)

Async variant of `wrap_model_call`.

## Signature

```python
awrap_model_call(
    self,
    request: ModelRequest[Any],
    handler: Callable[[ModelRequest[Any]], Awaitable[ModelCallResult]],
) -> ModelCallResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L1078)
