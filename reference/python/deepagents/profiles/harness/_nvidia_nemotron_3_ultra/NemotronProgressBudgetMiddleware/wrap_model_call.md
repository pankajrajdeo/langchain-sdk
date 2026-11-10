---
title: "wrap_model_call"
description: "Short-circuit before another model call if progress budgets are exhausted."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronProgressBudgetMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, nemotronprogressbudgetmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronProgressBudgetMiddleware/wrap_model_call)

Short-circuit before another model call if progress budgets are exhausted.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[Any],
    handler: Callable[[ModelRequest[Any]], ModelCallResult],
) -> ModelCallResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/18930b5463c8a0a432353db5299af280f879973f/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L1066)
