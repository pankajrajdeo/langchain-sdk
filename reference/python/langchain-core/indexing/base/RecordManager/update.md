---
title: "update"
description: "Upsert records into the database."
source: "https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/update"
category: "reference"
tags: [reference, langchain-core, indexing, base, recordmanager, update]
---

# update

> **Method** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/indexing/base/RecordManager/update)

Upsert records into the database.

## Signature

```python
update(
    self,
    keys: Sequence[str],
    *,
    group_ids: Sequence[str | None] | None = None,
    time_at_least: float | None = None,
) -> None
```

## Parameters

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `keys` | `Sequence[str]` | Yes | A list of record keys to upsert. |
| `group_ids` | `Sequence[str \| None] \| None` | No | A list of group IDs corresponding to the keys. (default: `None`) |
| `time_at_least` | `float \| None` | No | Optional timestamp. Implementation can use this to optionally verify that the timestamp IS at least this time in the system that stores the data.  e.g., use to validate that the time in the postgres database is equal to or larger than the given timestamp, if not raise an error.  This is meant to help prevent time-drift issues since time may not be monotonically increasing! (default: `None`) |

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/c5ab14d42a3e22865c9def909de0b11d70b0bbf0/libs/core/langchain_core/indexing/base.py#L98)
