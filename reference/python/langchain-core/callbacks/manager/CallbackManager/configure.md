---
title: "configure"
description: "Configure the callback manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/configure"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, callbackmanager, configure]
---

# configure

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/CallbackManager/configure)

Configure the callback manager.

## Signature

```python
configure(
    cls,
    inheritable_callbacks: Callbacks = None,
    local_callbacks: Callbacks = None,
    verbose: bool = False,
    inheritable_tags: list[str] | None = None,
    local_tags: list[str] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
    local_metadata: dict[str, Any] | None = None,
    *,
    langsmith_inheritable_metadata: Mapping[str, Any] | None = None,
    langsmith_inheritable_tags: list[str] | None = None,
) -> CallbackManager
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `inheritable_callbacks` | `Callbacks` | No | The inheritable callbacks. (default: `None`) |
| `local_callbacks` | `Callbacks` | No | The local callbacks. (default: `None`) |
| `verbose` | `bool` | No | Whether to enable verbose mode. (default: `False`) |
| `inheritable_tags` | `list[str] \| None` | No | The inheritable tags. (default: `None`) |
| `local_tags` | `list[str] \| None` | No | The local tags. (default: `None`) |
| `inheritable_metadata` | `dict[str, Any] \| None` | No | The inheritable metadata. (default: `None`) |
| `local_metadata` | `dict[str, Any] \| None` | No | The local metadata. (default: `None`) |
| `langsmith_inheritable_metadata` | `Mapping[str, Any] \| None` | No | Default inheritable metadata applied to any `LangChainTracer` handlers via `set_defaults`. (default: `None`) |
| `langsmith_inheritable_tags` | `list[str] \| None` | No | Default inheritable tags applied to any `LangChainTracer` handlers via `set_defaults`. (default: `None`) |

## Returns

`CallbackManager`

The configured callback manager.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/callbacks/manager.py#L1693)
