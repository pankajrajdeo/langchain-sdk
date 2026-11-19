---
title: "exit_code"
description: "The process exit code."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteResponse/exit_code"
category: "reference"
tags: [reference, deepagents, backends, protocol, executeresponse, exit_code]
---

# exit_code

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteResponse/exit_code)

The process exit code.

0 indicates success, non-zero indicates failure. `None` means the exit code
could not be determined.

## Signature

```python
exit_code: int | None = None
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/9b754bc914cc75c3f6d8c6e99353e81041b73bce/libs/deepagents/deepagents/backends/protocol.py#L831)
