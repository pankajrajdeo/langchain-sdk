---
title: "aedit"
description: "Async version of edit, delegating to aexecute and aupload_files."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aedit"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, aedit]
---

# aedit

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aedit)

Async version of `edit`, delegating to `aexecute` and `aupload_files`.

## Signature

```python
aedit(
    self,
    file_path: str,
    old_string: str,
    new_string: str,
    replace_all: bool = False,
) -> EditResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9ea3f1912abd8b7eecb504d78ef99fcf279bf561/libs/deepagents/deepagents/backends/sandbox.py#L1873)
