---
title: "result"
description: "View source on GitHub"
source: "https://reference.langchain.com/python/deepagents/middleware/rubric/GraderResponse/result"
category: "reference"
tags: [reference, deepagents, middleware, rubric, graderresponse, result]
---

# result

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/middleware/rubric/GraderResponse/result)

## Signature

```python
result: GraderVerdict = Field(description="Terminal verdict for this evaluation. Use 'satisfied' only when every criterion passes; 'needs_revision' when at least one criterion fails; 'failed' when the rubric cannot be evaluated.")
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/middleware/rubric.py#L313)
