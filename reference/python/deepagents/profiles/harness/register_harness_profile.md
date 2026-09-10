---
title: "register_harness_profile"
description: "Register a harness profile for a provider or specific model."
source: "https://reference.langchain.com/python/deepagents/profiles/harness/register_harness_profile"
category: "reference"
tags: [reference, deepagents, profiles, harness, register_harness_profile]
---

# register_harness_profile

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/harness/harness_profiles/register_harness_profile)

Register a harness profile for a provider or specific model.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../versioning.md)
    for more details.

Accepts either a runtime `HarnessProfile` or a declarative
`HarnessProfileConfig`. Config objects are converted to runtime profiles
at registration time so YAML/JSON-backed callers do not need a separate
manual conversion step.

Registrations are **additive**: if a profile is already registered under
`key` (including a built-in profile loaded during lazy bootstrap), the new
profile is merged on top rather than replacing it. The incoming profile's
fields win on conflicts; unspecified fields inherit from the existing
profile. Excluded-tool sets union, middleware sequences merge by type, and
`general_purpose_subagent` settings merge field-wise.

To extend an existing registration, call `register_harness_profile` again
under the same key:

```python
from deepagents import HarnessProfile, register_harness_profile

# Layer a system-prompt suffix on top of the previous registration.
register_harness_profile(
    "openai:gpt-5.4",
    HarnessProfile(system_prompt_suffix="Respond in under 100 words."),
)
```

## Signature

```python
register_harness_profile(
    key: str,
    profile: HarnessProfile | HarnessProfileConfig,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `key` | `str` | Yes | Either a provider name (no colon) for provider-wide defaults, or a full `provider:model` spec for a per-model override. Valid shapes:  - `"openai"` — provider-wide - `"openai:gpt-5.4"` — specific model |
| `profile` | `HarnessProfile \| HarnessProfileConfig` | Yes | The runtime harness profile or declarative config to register. |

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/profiles/harness/harness_profiles.py#L980)
