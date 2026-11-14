---
title: "glob"
description: "Structured glob matching returning GlobResult."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/glob"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, glob]
---

# glob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/glob)

Structured glob matching returning `GlobResult`.

Returned paths are absolute (see `_absolutize_glob_path`), which
`_check_fs_permission` relies on to apply `deny` rules.

## Signature

```python
glob(
    self,
    pattern: str,
    path: str | None = None,
) -> GlobResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/backends/sandbox.py#L2120)
