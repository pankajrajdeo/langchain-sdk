---
title: "write"
description: "Write content to a file, creating it or overwriting it if it already exists."
source: "https://reference.langchain.com/python/deepagents/backends/state/StateBackend/write"
category: "reference"
tags: [reference, deepagents, backends, state, statebackend, write]
---

# write

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/write)

Write content to a file, creating it or overwriting it if it already exists.

The update is queued directly via `CONFIG_KEY_SEND`.

## Signature

```python
write(
    self,
    file_path: str,
    content: str,
) -> WriteResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/state.py#L206)
