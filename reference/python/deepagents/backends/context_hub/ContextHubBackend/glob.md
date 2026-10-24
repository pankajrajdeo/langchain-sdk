---
title: "glob"
description: "Return files under path matching pattern."
source: "https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/glob"
category: "reference"
tags: [reference, deepagents, backends, context_hub, contexthubbackend, glob]
---

# glob

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/glob)

Return files under `path` matching `pattern`.

Matching uses the shared backend contract (`compile_grep_include_glob`)
on each path relative to `path`, so a bare pattern matches the basename
at any depth, a pattern with `/` matches the relative path, and a leading
`/` anchors. Plain `fnmatch` would diverge on all three: its `*` crosses
`/`, so `/*.py` would widen to every depth instead of anchoring to the
top level. When `path` names a file, only that file is considered.

A pattern written from the repo root also matches, so callers that
scoped a glob in the pattern before `path` was honored keep working.

## Signature

```python
glob(
    self,
    pattern: str,
    path: str | None = None,
) -> GlobResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/context_hub.py#L643)
