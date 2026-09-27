---
title: "GraderVerdict"
description: "Verdict the grader sub-agent emits via structured output."
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/GraderVerdict"
category: "reference"
tags: [reference, deepagents, middleware, rubric, graderverdict]
---

# GraderVerdict

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/GraderVerdict)

Verdict the grader sub-agent emits via structured output.

- `satisfied`: every criterion passes.
- `needs_revision`: at least one criterion fails; loop continues.
- `failed`: the rubric itself is malformed or impossible to evaluate
    against the transcript.

## Signature

```python
GraderVerdict = Literal['satisfied', 'needs_revision', 'failed']
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/bb49cf50d3450a3bbebe8d25240cb7ef6379bd0d/libs/deepagents/deepagents/middleware/rubric.py#L66)
