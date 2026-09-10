---
title: "edit"
description: "Edit a file by replacing string occurrences."
source: "https://reference.langchain.com/python/deepagents/backends/state/StateBackend/edit"
category: "reference"
tags: [reference, deepagents, backends, state, statebackend, edit]
---

# edit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/state/StateBackend/edit)

Edit a file by replacing string occurrences.

The update is queued directly via `CONFIG_KEY_SEND`.

## Signature

```python
edit(
    self,
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> EditResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/state.py#L222)
