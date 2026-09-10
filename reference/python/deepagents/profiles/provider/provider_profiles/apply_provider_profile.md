---
title: "apply_provider_profile"
description: "Compose init_chat_model kwargs from the registered profile for spec."
source: "https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/apply_provider_profile"
category: "reference"
tags: [reference, deepagents, profiles, provider, provider_profiles, apply_provider_profile]
---

# apply_provider_profile

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/profiles/provider/provider_profiles/apply_provider_profile)

Compose `init_chat_model` kwargs from the registered profile for `spec`.

!!! beta

    `deepagents.profiles` exposes beta APIs that may receive minor changes in
    future releases. Refer to the [versioning documentation](../../../../../../versioning.md)
    for more details.

This is the recommended entry point for honoring `ProviderProfile`
registrations when building a chat model — it composes lookup, `pre_init`
invocation, and kwargs merging into a single call. `get_provider_profile`
only returns the registered object; pair it with this helper (or call
this helper directly) any time you intend to actually instantiate a
model. Used by `resolve_model` and intended for any harness that layers
config-file values on top of SDK defaults.

Looks up the profile via `get_provider_profile`, runs its `pre_init` hook
(unless suppressed), and returns a fresh dict combining `init_kwargs`,
`init_kwargs_factory()` output, and `kwargs`. Caller-supplied `kwargs`
take highest precedence — profile defaults sit beneath them — so
user-provided values from config files or explicit overrides are never
silently replaced.

When no profile is registered for `spec`, returns a copy of `kwargs`
unchanged. This keeps the helper safe to call unconditionally.

## Signature

```python
apply_provider_profile(
    spec: str,
    kwargs: Mapping[str, Any] | None = None,
    *,
    run_pre_init: bool = True,
) -> dict[str, Any]
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `spec` | `str` | Yes | Model spec in `provider:model` format, or a bare provider/model identifier.  Same shape accepted by `get_provider_profile`. |
| `kwargs` | `Mapping[str, Any] \| None` | No | Caller-supplied kwargs that override profile defaults on shared keys.  Defaults to an empty mapping. (default: `None`) |
| `run_pre_init` | `bool` | No | When `True` (default), invokes the profile's `pre_init` hook before composing kwargs.  Set `False` to inspect the merged kwargs without firing side effects (e.g. dry-run, validation). (default: `True`) |

## Returns

`dict[str, Any]`

A fresh `dict` ready to spread into `init_chat_model`.

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/profiles/provider/provider_profiles.py#L318)
