---
title: "num_deleted"
description: "The number of items that were successfully deleted."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/DeleteResponse/num_deleted"
category: "reference"
tags: [reference, langchain-core, indexing, base, deleteresponse, num_deleted]
---

# num_deleted

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/DeleteResponse/num_deleted)

The number of items that were successfully deleted.

If returned, this should only include *actual* deletions.

If the ID did not exist to begin with,
it should not be included in this count.

## Signature

```python
num_deleted: int
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/1a41b51b0295d7cc6df45cdede199b4a34649b1d/libs/core/langchain_core/indexing/base.py#L467)
