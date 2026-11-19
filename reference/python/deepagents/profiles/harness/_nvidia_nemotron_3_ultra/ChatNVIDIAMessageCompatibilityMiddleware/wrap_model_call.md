---
title: "wrap_model_call"
description: "Patch request messages before ChatNVIDIA serializes them."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ChatNVIDIAMessageCompatibilityMiddleware/wrap_model_call"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, chatnvidiamessagecompatibilitymiddleware, wrap_model_call]
---

# wrap_model_call

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ChatNVIDIAMessageCompatibilityMiddleware/wrap_model_call)

Patch request messages before ChatNVIDIA serializes them.

## Signature

```python
wrap_model_call(
    self,
    request: ModelRequest[Any],
    handler: Callable[[ModelRequest[Any]], ModelCallResult],
) -> ModelCallResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L651)
