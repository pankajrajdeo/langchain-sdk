---
title: "download_files"
description: "Download files as raw bytes. Missing paths return file_not_found."
source: "https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/download_files"
category: "reference"
tags: [reference, deepagents, backends, context_hub, contexthubbackend, download_files]
---

# download_files

> **Method** in `deepagents`

📖 [View in docs](https://reference.langchain.com/python/deepagents/backends/context_hub/ContextHubBackend/download_files)

Download files as raw bytes. Missing paths return `file_not_found`.

## Signature

```python
download_files(
    self,
    paths: list[str],
) -> list[FileDownloadResponse]
```

---

[View source on GitHub](https://github.com/langchain-ai/deepagents/blob/4394bcd00b8eb46e7c423939643a0dfcfb5d8773/libs/deepagents/deepagents/backends/context_hub.py#L696)
