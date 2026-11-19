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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/backends/utils.py#L166)
