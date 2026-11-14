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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/c858b3641b13fb3f40fe3a12515517b81fb8a744/libs/deepagents/deepagents/backends/protocol.py#L831)
