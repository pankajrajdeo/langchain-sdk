---
title: "validate_profile_key"
description: "Validate a profile registry key."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/validate_profile_key"
category: "reference"
tags: [reference, deepagents, profiles, provider, provider_profiles, validate_profile_key]
---

# validate_profile_key

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/_keys/validate_profile_key)

Validate a profile registry key.

Enforces the `provider` or `provider:model` shape used by the lookup
functions. Rejects empty strings, whitespace-only or whitespace-padded
halves, multiple colons, and empty halves.

## Signature

```python
validate_profile_key(
    key: str,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | The registry key to check. |

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/profiles/_keys.py#L11)
