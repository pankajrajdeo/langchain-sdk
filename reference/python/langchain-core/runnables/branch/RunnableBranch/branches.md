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

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/runnables/branch.py#L70)
