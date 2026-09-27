---
title: "get_time"
description: "Get the current server time as a high resolution timestamp!"
source: "https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/get_time"
category: "reference"
tags: [reference, langchain-core, indexing, base, recordmanager, get_time]
---

# get_time

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/get_time)

Get the current server time as a high resolution timestamp!

It's important to get this from the server to ensure a monotonic clock,
otherwise there may be data loss when cleaning up old documents!

## Signature

```python
get_time(
    self,
) -> float
```

## Returns

`float`

The current server time as a float timestamp.

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/indexing/base.py#L76)
