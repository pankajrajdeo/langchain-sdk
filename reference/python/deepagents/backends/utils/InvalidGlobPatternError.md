---
title: "InvalidGlobPatternError"
description: "A glob pattern the shared matcher refuses to compile."
source: "https://reference.langchain.com/python/deepagents/backends/utils/InvalidGlobPatternError"
category: "reference"
tags: [reference, deepagents, backends, utils, invalidglobpatternerror]
---

# InvalidGlobPatternError

> **Class** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/InvalidGlobPatternError)

A glob pattern the shared matcher refuses to compile.

Subclasses `ValueError` so existing `except ValueError` handlers keep
working. Callers that catch this specific type can label the failure a
*pattern* problem truthfully -- a bare `ValueError` from the same call also
covers path normalization, and mislabeling one as the other sends the model
off rewriting a glob that was fine.

## Signature

```python
InvalidGlobPatternError()
```

## Extends

- `ValueError`

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/utils.py#L26)
