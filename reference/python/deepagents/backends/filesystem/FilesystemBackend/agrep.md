---
title: "agrep"
description: "Async version of grep, with optional surrounding context lines."
source: "https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/agrep"
category: "reference"
tags: [reference, deepagents, backends, filesystem, filesystembackend, agrep]
---

# agrep

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/filesystem/FilesystemBackend/agrep)

Async version of `grep`, with optional surrounding context lines.

As in the base `agrep`, the async timeout bounds how long the caller
waits; it does not stop the worker thread spawned by `asyncio.to_thread`.

## Signature

```python
agrep(
    self,
    pattern: str,
    path: str | None = None,
    glob: str | None = None,
    *,
    max_count: int | None = None,
    context_lines: int = 0,
) -> GrepResult
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/filesystem.py#L864)
