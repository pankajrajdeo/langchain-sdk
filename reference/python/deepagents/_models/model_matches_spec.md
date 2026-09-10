---
title: "model_matches_spec"
description: "Check whether a model instance already matches a string model spec."
source: "https://reference.langchain.com/python/deepagents/_models/model_matches_spec"
category: "reference"
tags: [reference, deepagents, models, model_matches_spec]
---

# model_matches_spec

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/_models/model_matches_spec)

Check whether a model instance already matches a string model spec.

Bare specs match by model identifier. Provider-prefixed specs match by both
model identifier and provider when the current model exposes a provider via
`_get_ls_params`; if the provider cannot be inspected, the check falls back
to identifier-only matching for backwards compatibility with custom models.
Provider comparison is normalized, so case, hyphen/underscore spelling, and
known aliases do not read as a mismatch (see `_normalize_provider`).

Assumes the `provider:model` convention (single colon separator).

## Signature

```python
model_matches_spec(
    model: BaseChatModel,
    spec: str,
) -> bool
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `model` | `BaseChatModel` | Yes | Chat model instance to inspect. |
| `spec` | `str` | Yes | Model spec in `provider:model` format (e.g., `openai:gpt-5`). |

## Returns

`bool`

`True` if the model already matches the spec, otherwise `False`.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/_models.py#L146)
