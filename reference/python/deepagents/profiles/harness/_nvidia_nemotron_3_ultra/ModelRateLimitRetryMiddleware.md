---
title: "ModelRateLimitRetryMiddleware"
description: "Retry transient provider 429s around model calls."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ModelRateLimitRetryMiddleware"
category: "reference"
tags: [reference, deepagents, profiles, harness, nvidia_nemotron_3_ultra, modelratelimitretrymiddleware]
---

# ModelRateLimitRetryMiddleware

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ModelRateLimitRetryMiddleware)

Retry transient provider 429s around model calls.

## Signature

```python
ModelRateLimitRetryMiddleware(
    self,
    retry_delays: tuple[float, ...] = _RATE_LIMIT_RETRY_DELAYS,
)
```

## Extends

- `AgentMiddleware`

## Constructors

```python
__init__(
    self,
    retry_delays: tuple[float, ...] = _RATE_LIMIT_RETRY_DELAYS,
) -> None
```

| Name | Type |
|------|------|
| `retry_delays` | `tuple[float, ...]` |

## Properties

- `name`

## Methods

- [`wrap_model_call()`](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ModelRateLimitRetryMiddleware/wrap_model_call)
- [`awrap_model_call()`](https://reference.langchain.com/python/deepagents/profiles/harness/_nvidia_nemotron_3_ultra/ModelRateLimitRetryMiddleware/awrap_model_call)

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/profiles/harness/_nvidia_nemotron_3_ultra.py#L219)
