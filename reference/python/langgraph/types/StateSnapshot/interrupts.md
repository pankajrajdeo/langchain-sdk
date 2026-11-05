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

[View source on GitHub](https://github.com/langchain-ai/langgraph/blob/a4d4187e82cdb0a73d68c76d70d655dd73a6db0b/libs/langgraph/langgraph/types.py#L738)
