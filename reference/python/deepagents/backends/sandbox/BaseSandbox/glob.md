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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/sandbox.py#L2120)
