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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/backends/sandbox.py#L1812)
