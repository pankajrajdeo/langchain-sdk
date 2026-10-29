---
title: "on_chain_error"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_chain_error"
category: "reference"
tags: [reference, langchain-core, tracers, base, asyncbasetracer, on_chain_error]
---

# on_chain_error

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/base/AsyncBaseTracer/on_chain_error)

## Signature

```python
on_chain_error(
    self,
    error: BaseException,
    *,
    inputs: dict[str, Any] | None = None,
    run_id: UUID,
    kwargs: Any = {},
) -> None
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/tracers/base.py#L763)
