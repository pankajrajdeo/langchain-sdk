---
title: "download_files"
description: "Download multiple files from the sandbox."
source: "https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/download_files"
category: "reference"
tags: [reference, deepagents, backends, sandbox, basesandbox, download_files]
---

# download_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/sandbox/BaseSandbox/download_files)

Download multiple files from the sandbox.

Implementations must support partial success - catch exceptions per-file
and return errors in `FileDownloadResponse` objects rather than raising.

## Signature

```python
download_files(
    self,
    paths: list[str],
) -> list[FileDownloadResponse]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/53e090968118f72f6dd3847d097607461a0fb5a8/libs/deepagents/deepagents/backends/sandbox.py#L2171)
