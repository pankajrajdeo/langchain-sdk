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

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/42adc1bca1147715ac58fad49bc74c12fa63bb84/libs/deepagents/deepagents/backends/sandbox.py#L2171)
