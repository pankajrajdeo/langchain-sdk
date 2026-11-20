---
title: "branches"
description: "A list of (condition, Runnable) pairs."
source: "https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/branches"
category: "reference"
tags: [reference, langchain-core, runnables, branch, runnablebranch, branches]
---

# branches

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/runnables/branch/RunnableBranch/branches)

A list of `(condition, Runnable)` pairs.

## Signature

```python
branches: Sequence[tuple[Runnable[Input, bool], Runnable[Input, Output]]]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/d4dafe5839c4a6b07d71cc78697df0de9e627e21/libs/core/langchain_core/runnables/branch.py#L70)
