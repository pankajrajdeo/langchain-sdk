---
title: "offloaded"
description: "Whether the output was left at the capture path."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteOffloadResult/offloaded"
category: "reference"
tags: [reference, deepagents, backends, protocol, executeoffloadresult, offloaded]
---

# offloaded

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ExecuteOffloadResult/offloaded)

Whether the output was left at the capture path.

When `True`, `response.output` holds only a preview of the output and the
full output lives at the capture path on the sandbox filesystem.

When `False`, `response.output` is the complete output.

## Signature

```python
offloaded: bool
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/protocol.py#L864)
