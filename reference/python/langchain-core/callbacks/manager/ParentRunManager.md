---
title: "ParentRunManager"
description: "Synchronous parent run manager."
source: "https://reference.langchain.com/python/langchain-core/callbacks/manager/ParentRunManager"
category: "reference"
tags: [reference, langchain-core, callbacks, manager, parentrunmanager]
---

# ParentRunManager

> **Class** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/callbacks/manager/ParentRunManager)

Synchronous parent run manager.

## Signature

```python
ParentRunManager(
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

- `RunManager`

## Methods

- [`get_child()`](https://reference.langchain.com/python/langchain-core/callbacks/manager/ParentRunManager/get_child)

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/864754c5e293fba981302408fa3e2cf2f5f2d889/libs/core/langchain_core/callbacks/manager.py#L610)
