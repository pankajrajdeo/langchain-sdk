---
title: "aexecute_with_offload"
description: "Async version of execute_with_offload, delegating to aexecute."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aexecute_with_offload"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, aexecute_with_offload]
---

# aexecute_with_offload

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/aexecute_with_offload)

Async version of `execute_with_offload`, delegating to `aexecute`.

## Signature

```python
aexecute_with_offload(
    self,
    command: str,
    capture_path: str,
    *,
    max_inline_bytes: int,
    max_capture_bytes: int | None = None,
    timeout: int | None = None,
) -> ExecuteOffloadResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/e85c6b98087861512d2c5240305e16cfac68a746/libs/deepagents/deepagents/backends/sandbox.py#L1685)
