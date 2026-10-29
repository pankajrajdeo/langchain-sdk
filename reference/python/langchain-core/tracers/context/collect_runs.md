---
title: "collect_runs"
description: "Collect all run traces in context."
source: "https://reference.langchain.com/python/langchain-core/tracers/context/collect_runs"
category: "reference"
tags: [reference, langchain-core, tracers, context, collect_runs]
---

# collect_runs

> **Function** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/context/collect_runs)

Collect all run traces in context.

## Signature

```python
collect_runs() -> Generator[RunCollectorCallbackHandler, None, None]
```

## Description

**Example:**

>>> with collect_runs() as runs_cb:
chain.invoke("foo")
run_id = runs_cb.traced_runs[0].id

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/6419339aa163a49f32d9b80ff20d6adc3b446d49/libs/core/langchain_core/tracers/context.py#L93)
