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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/a4b4a7b9a6d8b5eb2352e26e110f1b7beffc6f62/libs/core/langchain_core/tracers/context.py#L93)
