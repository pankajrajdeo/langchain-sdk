---
title: "interrupts"
description: "Interrupts that occurred in this step."
source: "https://reference.langchain.com/python/langgraph/types/StateSnapshot/interrupts"
category: "reference"
tags: [reference, langgraph, types, statesnapshot, interrupts]
---

# interrupts

> **Attribute** in `langgraph`

📖 [View in docs](https://reference.langchain.com/python/langgraph/types/StateSnapshot/interrupts)

Interrupts that occurred in this step.

When reading the latest state (`get_state` without a `checkpoint_id`), this
contains only interrupts still waiting for an answer. When reading a specific
checkpoint or state history, it contains the most recent interrupt each task
raised in that step, including ones answered later in the same step.

## Signature

```python
interrupts: tuple[Interrupt, ...]
```

---

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/4c52e129eb1ab69a3da58b799f67929f77d81149/libs/langgraph/langgraph/types.py#L728)
