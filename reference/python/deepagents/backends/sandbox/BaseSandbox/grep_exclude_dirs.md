---
title: "grep_exclude_dirs"
description: "Directory names grep skips at any depth while searching."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/grep_exclude_dirs"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, grep_exclude_dirs]
---

# grep_exclude_dirs

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/grep_exclude_dirs)

Directory names `grep` skips at any depth while searching.

`.git` is skipped by default: it holds compressed object packs that cannot
hold a useful literal match yet make up most of a repository's bytes, so
searching a checkout reads it in full. Subclasses can extend the tuple (for
example with `node_modules`) or set it to `()` to search everything. A
search rooted at one of these directories still searches it.

## Signature

```python
grep_exclude_dirs: tuple[str, ...] = ('.git',)
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/0ec42441901968a75202a3ef365650eb280a473b/libs/deepagents/deepagents/backends/sandbox.py#L1609)
