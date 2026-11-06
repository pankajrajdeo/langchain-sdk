---
title: "after_agent"
description: "Loop once when final text needs ID resolution or branch rebinding."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/EntityResolutionGuardMiddleware/after_agent"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, entityresolutionguardmiddleware, after_agent]
---

# after_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/EntityResolutionGuardMiddleware/after_agent)

Loop once when final text needs ID resolution or branch rebinding.

## Signature

```python
after_agent(
    self,
    state: AgentState[Any],
    runtime: Runtime[Any],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L1653)
