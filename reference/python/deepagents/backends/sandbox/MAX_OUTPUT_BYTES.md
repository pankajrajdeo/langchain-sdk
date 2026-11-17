---
title: "MAX_OUTPUT_BYTES"
description: "Maximum size of rendered text content returned by read()."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/MAX_OUTPUT_BYTES"
category: "reference"
tags: [reference, deepagents, backends, sandbox, max_output_bytes]
---

# MAX_OUTPUT_BYTES

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/MAX_OUTPUT_BYTES)

Maximum size of rendered text content returned by `read()`.

Pages exceeding this cap are truncated and `TRUNCATION_MSG` is appended.
Mirrors the `MAX_OUTPUT_BYTES` literal in `_READ_COMMAND_TEMPLATE`.

## Signature

```python
MAX_OUTPUT_BYTES: Final = 500 * 1024
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/sandbox.py#L488)
