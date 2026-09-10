---
title: "wrap_model_call"
description: "Strip reasoning tags after the model returns."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronReasoningTagCleanupMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, nemotronreasoningtagcleanupmiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/NemotronReasoningTagCleanupMiddleware/wrap_model_call)

Strip reasoning tags after the model returns.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[Any],
    handler: Callable[[ModelRequest[Any]], ModelCallResult],
) -> ModelCallResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L670)
