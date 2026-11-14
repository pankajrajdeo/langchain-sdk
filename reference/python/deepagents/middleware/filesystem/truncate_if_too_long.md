---
title: "truncate_if_too_long"
description: "Truncate list or string result if it exceeds token limit (rough estimate: 4 chars/token)."
source: "https://reference.langchain.com/python/deepagents/middleware/filesystem/truncate_if_too_long"
category: "reference"
tags: [reference, deepagents, middleware, filesystem, truncate_if_too_long]
---

# truncate_if_too_long

> **Function** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/utils/truncate_if_too_long)

Truncate list or string result if it exceeds token limit (rough estimate: 4 chars/token).

## Signature

```python
truncate_if_too_long(
    result: list[str] | str,
) -> list[str] | str
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/backends/utils.py#L765)
