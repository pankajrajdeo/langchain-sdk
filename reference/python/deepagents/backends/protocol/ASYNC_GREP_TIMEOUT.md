---
title: "ASYNC_GREP_TIMEOUT"
description: "Timeout in seconds for the async grep wrapper."
source: "https://reference.langchain.com/python/deepagents/backends/protocol/ASYNC_GREP_TIMEOUT"
category: "reference"
tags: [reference, deepagents, backends, protocol, async_grep_timeout]
---

# ASYNC_GREP_TIMEOUT

> **Attribute** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/protocol/ASYNC_GREP_TIMEOUT)

Timeout in seconds for the async grep wrapper.

This gives `FilesystemBackend` enough headroom to finish the worst-case sync
path: ripgrep timeout, then Python fallback timeout.

## Signature

```python
ASYNC_GREP_TIMEOUT: Final = 2 * DEFAULT_GREP_TIMEOUT + 5
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/backends/protocol.py#L23)
