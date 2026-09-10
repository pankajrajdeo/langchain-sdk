---
title: "TRUNCATION_MSG"
description: "Sentinel appended to read() content when MAX_OUTPUT_BYTES is hit."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/TRUNCATION_MSG"
category: "reference"
tags: [reference, deepagents, backends, sandbox, truncation_msg]
---

# TRUNCATION_MSG

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/TRUNCATION_MSG)

Sentinel appended to `read()` content when `MAX_OUTPUT_BYTES` is hit.

## Signature

```python
TRUNCATION_MSG: Final = '\n\n[Output was truncated due to size limits. This paginated read result exceeded the sandbox stdout limit. Continue reading with a larger offset or smaller limit to inspect the rest of the file.]'
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/1aae3746682a65c837c5dd0f165b685253fe9465/libs/deepagents/deepagents/backends/sandbox.py#L486)
