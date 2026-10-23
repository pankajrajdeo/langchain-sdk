---
title: "AsyncRunManager"
description: "Async run manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncRunManager"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, asyncrunmanager]
---

# AsyncRunManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncRunManager)

Async run manager.

## Signature

```python
AsyncRunManager(
    self,
    *,
    run_id: UUID,
    handlers: list[BaseCallbackHandler],
    inheritable_handlers: list[BaseCallbackHandler],
    parent_run_id: UUID | None = None,
    tags: list[str] | None = None,
    inheritable_tags: list[str] | None = None,
    metadata: dict[str, Any] | None = None,
    inheritable_metadata: dict[str, Any] | None = None,
)
```

## Extends

- `BaseRunManager`
- `ABC`

## Methods

- [`get_sync()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncRunManager/get_sync)
- [`on_text()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncRunManager/on_text)
- [`on_retry()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/AsyncRunManager/on_retry)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/f4e6cde98d85910cef5d1f43e26e7a497ae861f3/libs/core/langchain_core/callbacks/manager.py#L632)
