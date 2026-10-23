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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/protocol.py#L819)
