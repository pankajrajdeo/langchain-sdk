---
title: "succeeded"
description: "The IDs that were successfully deleted."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/DeleteResponse/succeeded"
category: "reference"
tags: [reference, langchain-core, indexing, base, deleteresponse, succeeded]
---

# succeeded

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/DeleteResponse/succeeded)

The IDs that were successfully deleted.

If returned, this should only include *actual* deletions.

If the ID did not exist to begin with,
it should not be included in this list.

## Signature

```python
succeeded: Sequence[str]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/indexing/base.py#L476)
