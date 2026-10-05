---
title: "after_agent"
description: "Loop once when the final answer misses concrete tool-derived details."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/FinalAnswerGuardMiddleware/after_agent"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, finalanswerguardmiddleware, after_agent]
---

# after_agent

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/FinalAnswerGuardMiddleware/after_agent)

Loop once when the final answer misses concrete tool-derived details.

## Signature

```python
after_agent(
    self,
    state: AgentState[Any],
    runtime: Runtime[Any],
) -> dict[str, Any] | None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L1742)
