---
title: "suppress_langchain_deprecation_warning"
description: "Suppress LangChain deprecation warnings within the current context."
source: "https://reference.langchain.com/python/langchain-core/prompts/base/suppress_langchain_deprecation_warning"
category: "reference"
tags: [reference, langchain-core, prompts, base, suppress_langchain_deprecation_warning]
---

# suppress_langchain_deprecation_warning

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/_api/deprecation/suppress_langchain_deprecation_warning)

Suppress LangChain deprecation warnings within the current context.

Silences warnings emitted through `warn_deprecated` and `@deprecated`. It does not
modify the global `warnings` filters, so calling `warnings.warn` directly with
`LangChainDeprecationWarning` is not suppressed; use `warnings.filterwarnings` for
that.

Suppression is stored in a context variable, not a process-wide filter. It
applies to the current thread or asyncio task, and to tasks or copied contexts
created inside the block (e.g. `asyncio.create_task`, `asyncio.to_thread`),
which keep it even after the block exits. Other threads are unaffected.

## Signature

```python
suppress_langchain_deprecation_warning() -> Generator[None, None, None]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/2b7ff14fb2021e6f4ee22f796a9b888eaacb5af9/libs/core/langchain_core/_api/deprecation.py#L466)
