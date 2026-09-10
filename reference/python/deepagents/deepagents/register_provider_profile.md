---
title: "register_provider_profile"
description: "Register a ProviderProfile for a provider or specific model."
source: "https://reference.langchain.com/python/deepagents/deepagents/register_provider_profile"
category: "reference"
tags: [reference, deepagents, register_provider_profile]
---

# register_provider_profile

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/register_provider_profile)

Register a `ProviderProfile` for a provider or specific model.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../versioning.md)
    for more details.

Registrations are **additive**: if a profile is already registered under
`key` (including a built-in profile loaded during lazy bootstrap), the new
profile is merged on top rather than replacing it. The incoming profile's
fields win on conflicts; unspecified fields inherit from the existing
profile.
`pre_init` callables chain (existing runs first), and `init_kwargs_factory`
callables chain — both factories are invoked at every resolution (base
first, then override) and their outputs merge with the override's values
winning on shared keys.

To layer additional kwargs onto a built-in profile, register under the
same provider key. To override a built-in default (e.g. disable the
OpenAI Responses API), set the conflicting key explicitly:

```python
from deepagents import ProviderProfile, register_provider_profile

# Adds temperature alongside the built-in `use_responses_api=True`.
register_provider_profile("openai", ProviderProfile(init_kwargs={"temperature": 0}))

# Explicitly disables Responses API for OpenAI. (This will break usage,
# this example is purely illustrative.)
register_provider_profile(
    "openai",
    ProviderProfile(init_kwargs={"use_responses_api": False}),
)
```

## Signature

```python
register_provider_profile(
    key: str,
    profile: ProviderProfile,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | Either a provider name (no colon) for provider-wide defaults, or a full `provider:model` spec for a per-model override. Valid shapes:  - `"openai"` — provider-wide - `"openai:gpt-5.4"` — specific model |
| `profile` | `ProviderProfile` | Yes | The provider profile to register. |

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/profiles/provider/provider_profiles.py#L195)
