---
title: "logs"
description: "Map of run names to sub-runs."
source: "https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunState/logs"
category: "reference"
tags: [reference, langchain-core, tracers, log_stream, runstate, logs]
---

# logs

> **Attribute** in `langchain_core`

📖 [View in docs](https://reference.langchain.com/python/langchain-core/tracers/log_stream/RunState/logs)

Map of run names to sub-runs.

If filters were supplied, this list will contain only the runs that matched the
filters.

## Signature

```python
logs: dict[str, LogEntry]
```

---

[View source on GitHub](https://github.com/langchain-ai/langchain/blob/8215039dea978372bd3fd95b88663a11b0159043/libs/core/langchain_core/tracers/log_stream.py#L107)
